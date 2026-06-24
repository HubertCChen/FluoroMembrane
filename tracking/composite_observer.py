from tracking.base_observer import (
    BaseObserver
)


class CompositeObserver(BaseObserver):

    def __init__(
        self,
        *observers
    ):

        self.observers = observers

    def begin(self):

        for observer in self.observers:

            observer.begin()

    def initialize_photon(
        self,
        photon
    ):

        for observer in self.observers:

            observer.initialize_photon(
                photon
            )

    def record_event(
        self,
        photon,
        interaction
    ):

        for observer in self.observers:

            observer.record_event(
                photon,
                interaction
            )

    def finalize_photon(
        self,
        photon
    ):

        for observer in self.observers:

            observer.finalize_photon(
                photon
            )

    def end(self):

        for observer in self.observers:

            observer.end()