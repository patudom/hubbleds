from cosmicds.utils import debounce
from hubbleds.state import StudentMeasurement
from contextlib import closing
from io import BytesIO
from astropy.io import fits
from hubbleds.state import GalaxyData, SpectrumData, LocalState
import datetime
from cosmicds.remote import BaseAPI
from cosmicds.state import GlobalState, BaseState
from solara import Reactive
from solara.lab import Ref
from functools import cached_property
from cosmicds.logger import setup_logger

logger = setup_logger("API")


ELEMENT_REST = {"H-α": 6562.79, "Mg-I": 5176.7}
DEBOUNCE_TIMEOUT = 1


class LocalAPI(BaseAPI):
    def get_galaxies(self, local_state: Reactive[LocalState]) -> list[GalaxyData]:
        galaxy_data_json = self.request_session.get(
            f"{self.API_URL}/{local_state.value.story_id}/galaxies?types=Sp"
        ).json()

        galaxy_data = [GalaxyData(**x) for x in galaxy_data_json]

        return galaxy_data

    def load_spectrum_data(
        self, gal_data: GalaxyData, local_state: Reactive[LocalState]
    ) -> SpectrumData:
        file_name = f"{gal_data.name.replace('.fits', '')}.fits"

        type_folders = {"Sp": "spiral", "E": "elliptical", "Ir": "irregular"}
        folder = type_folders[gal_data.type]
        url = (
            f"{self.API_URL}/{local_state.value.story_id}/spectra/{folder}/{file_name}"
        )
        response = self.request_session.get(url)

        with closing(BytesIO(response.content)) as f:
            f.name = gal_data.name

            with fits.open(f) as hdulist:
                data = hdulist["COADD"].data if "COADD" in hdulist else None

        if data is None:
            logger.error("No extension named 'COADD' in spectrum file.")
            return

        spec_data = SpectrumData(
            name=gal_data.name,
            wave=10 ** data["loglam"],
            flux=data["flux"],
            ivar=data["ivar"],
        )

        logger.info("Loaded spectrum data for galaxy `%s` from database.", gal_data.id)

        return spec_data

    def get_measurements(
        self, global_state: Reactive[GlobalState], local_state: Reactive[LocalState]
    ) -> list[StudentMeasurement]:
        url = (
            f"{self.API_URL}/{local_state.value.story_id}/measurements/"
            f"{global_state.value.student.id}"
        )
        r = self.request_session.get(url)
        measurement_json = r.json()

        measurements = Ref(local_state.fields.measurements)
        parsed_measurements = []

        for measurement in measurement_json["measurements"]:
            measurement = StudentMeasurement(**measurement)
            parsed_measurements.append(measurement)

        measurements.set(parsed_measurements)

        logger.info("Loaded measurements from database.")

        return measurements.value

    def get_sample_measurements(
        self, global_state: Reactive[GlobalState], local_state: Reactive[LocalState]
    ) -> list[StudentMeasurement]:
        r = self.request_session.get(
            f"{self.API_URL}/{local_state.value.story_id}/sample-"
            f"measurements/{global_state.value.student.id}"
        )

        sample_measurement_json = r.json()

        if len(sample_measurement_json["measurements"]) == 0:
            logger.info(
                "Failed to find sample galaxies for user `%s`: creating new "
                "sample measurement.",
                global_state.value.student.id,
            )
            sample_gal_data = LOCAL_API.get_sample_galaxy(local_state)
            sample_measurement_json["measurements"].append(
                StudentMeasurement(
                    student_id=global_state.value.student.id,
                    galaxy=sample_gal_data,
                ).dict()
            )

        sample_measurements = Ref(local_state.fields.example_measurements)
        parsed_sample_measurements = []

        for measurement in sample_measurement_json["measurements"]:
            measurement = StudentMeasurement(**measurement)
            parsed_sample_measurements.append(measurement)

        sample_measurements.set(parsed_sample_measurements)

        logger.info("Loaded example measurements from database.")

        return sample_measurements.value

    def put_measurements(
        self, global_state: Reactive[GlobalState], local_state: Reactive[LocalState]
    ):
        url = f"{self.API_URL}/{local_state.value.story_id}/submit-measurement/"

        for measurement in local_state.value.measurements:
            r = self.request_session.put(url, json=measurement.dict(exclude={"galaxy"}))

            if r.status_code != 200:
                logger.warning(
                    f"Failed to add measurement for galaxy `%s` by student `%s`.",
                    global_state.value.student.id,
                    measurement.galaxy_id,
                )

        logger.info(
            "Stored measurements for student `%s`.",
            global_state.value.student.id,
        )

    def put_sample_measurements(
        self, global_state: Reactive[GlobalState], local_state: Reactive[LocalState]
    ):
        url = f"{self.API_URL}/{local_state.value.story_id}/sample-measurement/"

        for measurement in local_state.value.example_measurements:
            logger.info(
                f"Adding example measurement for galaxy `%s` by student `%s`.",
                measurement.galaxy_id,
                global_state.value.student.id,
            )

            r = self.request_session.put(url, json=measurement.dict(exclude={"galaxy"}))

            if r.status_code != 200:
                logger.warning(
                    f"Failed to add example measurement for galaxy `%s` by student `%s`.",
                    measurement.galaxy_id,
                    global_state.value.student.id,
                )

        logger.info(
            "Stored example measurements for student %s.",
            global_state.value.student.id,
        )

    def get_measurement(
        self,
        galaxy_id: int,
        global_state: Reactive[GlobalState],
        local_state: Reactive[LocalState],
    ) -> StudentMeasurement:
        logger.info(
            "Retrieving measurement of galaxy %s for student %s...",
            (galaxy_id, global_state.value.student.id),
        )
        url = (
            f"{self.API_URL}/{local_state.value.story_id}/measurements/"
            f"{global_state.value.student.id}/{galaxy_id}"
        )
        measurement_json = self.request_session.get(url).json()
        measurement = measurement_json["measurements"]

        measurements = Ref(local_state.fields.measurements)

        measurements.set(measurements.value + [measurement])

        return measurement

    def get_sample_measurement(
        self,
        galaxy_id: int,
        global_state: Reactive[GlobalState],
        local_state: Reactive[LocalState],
    ) -> StudentMeasurement:
        logger.info(
            "Retrieving sample measurement of galaxy %s for student %s...",
            (galaxy_id, global_state.value.student.id),
        )
        url = (
            f"{self.API_URL}/{local_state.value.story_id}/"
            f"sample-measurements/{global_state.value.student.id}/"
            f"{galaxy_id}"
        )
        measurement_json = self.request_session.get(url).json()
        measurement = measurement_json["measurements"]

        measurements = Ref(local_state.fields.measurements)

        measurements.set(measurements.value + [measurement])

        return measurement

    def delete_all_measurements(
        self, global_state: Reactive[GlobalState], local_state: Reactive[LocalState]
    ):
        url = f"{self.API_URL}/{local_state.value.story_id}/measurements/{global_state.value.student.id}"
        measurements_json = self.request_session.get(url).json()

        for measurement in measurements_json["measurements"]:
            # url = url + "/first" if samples else url + f"/{measurement['galaxy']['id']}"
            url += f"/{measurement['galaxy']['id']}"
            r = self.request_session.delete(url)

            if r.status_code != 200:
                logger.error(
                    "Failed to delete measurement of galaxy `%s` for student `%s`.",
                    measurement["galaxy"]["id"],
                    global_state.value.student.id,
                )

    def get_sample_galaxy(self, local_state: Reactive[LocalState]) -> GalaxyData:
        galaxy_json = self.request_session.get(
            f"{self.API_URL}/{local_state.value.story_id}/sample-galaxy"
        ).json()

        galaxy_data = GalaxyData(**galaxy_json)

        return galaxy_data

    def put_stage_state(
        self,
        global_state: Reactive[GlobalState],
        local_state: Reactive[LocalState],
        component_state: Reactive[BaseState],
    ):
        logger.info("Serializing stage state into DB.")

        comp_state_dict = component_state.value.dict(
            exclude={"selected_galaxy", "selected_example_galaxy"}
        )
        comp_state_dict.update(
            {"current_step": component_state.value.current_step.value}
        )

        r = self.request_session.put(
            f"{self.API_URL}/stage-state/{global_state.value.student.id}/"
            f"{local_state.value.story_id}/{component_state.value.stage_id}",
            json=comp_state_dict,
        )

        if r.status_code != 200:
            logger.error("Failed to write story state to database.")

    def put_story_state(
        self,
        global_state: Reactive[GlobalState],
        local_state: Reactive[LocalState],
    ):
        logger.info("Serializing state into DB.")

        state = {
            "app": global_state.value.dict(),
            "story": local_state.value.dict(
                exclude={"measurements", "example_measurements"}
            ),
        }

        r = self.request_session.put(
            f"{self.API_URL}/story-state/{global_state.value.student.id}/{local_state.value.story_id}",
            json=state,
        )

        if r.status_code != 200:
            logger.error("Failed to write story state to database.")


LOCAL_API = LocalAPI()
