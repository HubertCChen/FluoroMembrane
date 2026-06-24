from sources.base_source import (
    BaseSource
)

from core.photon import (
    Photon
)

from core.vector import (
    Vector
)


class PointSource(BaseSource):

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

        self.next_id = 1

    def generate_photon(
        self
    ):

        photon = Photon(

            photon_id=self.next_id,

            position=self.position,

            direction=self.direction,

            wavelength=self.wavelength
        )

        self.next_id += 1

        return photon