from tracking.base_observer import (
    BaseObserver
)

from core.photon_event import (
    PhotonEvent
)


class EventObserver(BaseObserver):

    def __init__(self):

        # One history list per photon
        self.histories = []

    def initialize_photon(
        self,
        photon
    ):

        photon.history = []

    def record_event(
        self,
        photon,
        interaction
    ):

        photon.history.append(

            PhotonEvent(

                event_number=
                len(photon.history) + 1,

                event_type=
                interaction.interaction_type.value,

                position=
                interaction.position,

                distance=
                interaction.distance,

                surface=
                interaction.surface
            )
        )

    def finalize_photon(
        self,
        photon
    ):

        self.histories.append(
            photon.history.copy()
        )