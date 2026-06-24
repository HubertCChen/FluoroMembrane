from abc import ABC, abstractmethod


class BaseSource(ABC):

    @abstractmethod
    def generate_photon(
        self
    ):
        pass