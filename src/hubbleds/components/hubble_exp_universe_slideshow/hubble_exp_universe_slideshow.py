from solara import component_vue
from ...utils import IMAGE_BASE_URL

@component_vue("HubbleExpUniverseSlideshow.vue")
def HubbleExpUniverseSlideshow(
    dialog,
    step,
    maxStepCompleted,
    length=4,
    interactSteps=[1],
    titles=[
        "Hubble's Discovery",
        "A Running Race",
        "Runner's Velocities vs. Distances",
        "Age of the Universe"
    ],
    image_location=f"{IMAGE_BASE_URL}/stage_three",
    event_on_slideshow_finished=None,
    #pass in viewers when we have them
):
    pass