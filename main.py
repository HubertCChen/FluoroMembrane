from core.vector import Vector
from core.photon import Photon

from geometry.rectangular_film import (
    RectangularFilm
)

from physics.bounce import (
    bounce
)

film = RectangularFilm(
    width=0.210,
    length=0.297,
    thickness=0.0004,
    refractive_index=1.49
)

photon = Photon(
    photon_id=1,

    position=Vector(
        0.100,
        0.100,
        0.0002
    ),

    direction=Vector(
        1,
        0,
        1
    ).normalize(),

    wavelength=450
)

for step in range(5):

    interaction = bounce(
        photon,
        film
    )

    print(
        f"Step {step+1}"
    )

    print(
        interaction.surface
    )

    print(
        photon.position
    )

    print(
        photon.direction
    )

    print()