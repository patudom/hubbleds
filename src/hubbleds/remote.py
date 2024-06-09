from cosmicds.utils import API_URL
from cosmicds.state import GLOBAL_STATE
from .utils import HUBBLE_ROUTE_PATH
from .data_models.student import student_data, StudentMeasurement
from contextlib import closing
from io import BytesIO
from astropy.io import fits


class DatabaseAPI:
    def get_measurements(self):
        url = f"{API_URL}/{HUBBLE_ROUTE_PATH}/measurements/{GLOBAL_STATE.student.id.value}"
        r = GLOBAL_STATE.request_session.get(url)
        res_json = r.json()

        # Parse out the measured data
        measurements = []

        for measurement in res_json["measurements"]:
            meas_dict = {}

            for k, v in measurement.items():
                if not (k.endswith("_value") or k == "galaxy"):
                    continue

                meas_dict[k.replace("_value", "")] = v

                if k != "galaxy":
                    continue

                gal_dict = {}

                for gk, gv in v.items():
                    if gk == "galaxy_id":
                        gk = "id"

                    gal_dict[gk] = gv

                # Include the spectrum data as well
                gal_type = gal_dict["type"]
                gal_name = gal_dict["name"]
                folder = {"Sp": "spiral", "E": "elliptical", "Ir": "irregular"}.get(
                    gal_type
                )

                response = GLOBAL_STATE.request_session.get(
                    f"{API_URL}/{HUBBLE_ROUTE_PATH}/spectra/{folder}/{gal_name}"
                )

                with closing(BytesIO(response.content)) as f:
                    f.name = gal_name

                    with fits.open(f) as hdulist:
                        data = hdulist["COADD"].data if "COADD" in hdulist else None

                if data is None:
                    print("No extension named 'COADD' in spectrum fits file.")
                    return

                spec_data = dict(
                    name=gal_name,
                    wave=10 ** data["loglam"],
                    flux=data["flux"],
                    ivar=data["ivar"],
                )

                gal_dict["spectrum"] = spec_data

                meas_dict[k] = gal_dict

            measurements.append(StudentMeasurement(**meas_dict))

        return measurements

    def get_story_state(self):
        r = GLOBAL_STATE.request_session().get(f"{API_URL}/story-state/{GLOBAL_STATE.student.id.value}/{name}")
