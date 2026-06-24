from abc import ABC, abstractmethod


class BaseObserver(ABC):

    def begin(self):
        """
        Called once before the simulation starts.
        """
        pass

    @abstractmethod
    def initialize_photon(
        self,
        photon
    ):
        pass

    @abstractmethod
    def record_event(
        self,
        photon,
        interaction
    ):
        pass

    @abstractmethod
    def finalize_photon(
        self,
        photon
    ):
        pass

    def end(self):
        """
        Called once after the simulation ends.
        """
        pass