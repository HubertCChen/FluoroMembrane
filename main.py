from core.vector import Vector
from core.photon import Photon

from physics.propagation import propagate


photon = Photon(
    photon_id=1,

    position=Vector(
        0.0,
        0.0,
        0.0
    ),

    direction=Vector(
        0.0,
        0.0,
        1.0
    ).normalize(),

    wavelength=450
)

print("Initial position")
print(photon.position)

propagate(
    photon,
    0.001
)

print("After propagation")
print(photon.position)

print("Travel distance")
print(photon.travel_distance)