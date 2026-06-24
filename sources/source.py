from abc import ABC, abstractmethod


class Source(ABC):

    @abstractmethod
    def generate_photon(
        self,
        photon_id
    ):
        pass