from core.photon import Photon

from sources.source import Source


class PointSource(Source):

    def __init__(
        self,
        position,
        direction,
        wavelength
    ):

        self.position = position

        self.direction = (
            direction.normalize()
        )

        self.wavelength = wavelength

    def generate_photon(
        self,
        photon_id
    ):

        return Photon(
            photon_id=photon_id,

            position=self.position.copy(),

            direction=self.direction.copy(),

            wavelength=self.wavelength
        )