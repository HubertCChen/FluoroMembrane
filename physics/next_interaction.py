from geometry.ray_box import (
    next_boundary_interaction
)

from physics.absorption_interaction import (
    next_absorption_interaction
)


def next_interaction(
    photon,
    film,
    material
):

    boundary = (
        next_boundary_interaction(
            film,
            photon.position,
            photon.direction
        )
    )

    absorption = (
        next_absorption_interaction(
            photon,
            material
        )
    )

    interactions = [

        boundary,
        absorption

    ]

    interactions = [
        i for i in interactions
        if i is not None
    ]

    return min(
        interactions,
        key=lambda x: x.distance
    )