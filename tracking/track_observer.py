from tracking.base_observer import (
    BaseObserver
)

from storage.photon_result_builder import (
    build_photon_result
)


class TrackObserver(BaseObserver):

    def __init__(self):

        self.results = []

    def initialize_photon(
        self,
        photon
    ):

        photon.initial_position = (
            photon.position
        )

        photon.initial_direction = (
            photon.direction
        )

    def record_event(
        self,
        photon,
        interaction
    ):

        pass

    def finalize_photon(
        self,
        photon
    ):

        photon_result = build_photon_result(
            photon
        )

        self.results.append(
            photon_result
        )