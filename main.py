from core.vector import Vector
from core.photon import Photon

from materials.material import (
    Material
)

from physics.absorption_interaction import (
    next_absorption_interaction
)

photon = Photon(

    photon_id=1,

    position=Vector(
        0,
        0,
        0
    ),

    direction=Vector(
        1,
        0,
        0
    ),

    wavelength=450
)

material = Material(

    refractive_index=1.49,

    mu_abs=10,

    mu_scat=0
)

interaction = (
    next_absorption_interaction(
        photon,
        material
    )
)

print(interaction)