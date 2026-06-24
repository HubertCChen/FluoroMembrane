from geometry.ray_box import (
    next_boundary_interaction
)

from physics.reflection import (
    reflect
)

EPSILON = 1e-12


def bounce(
    photon,
    film
):

    interaction = (
        next_boundary_interaction(
            film,
            photon.position,
            photon.direction
        )
    )

    if interaction is None:
        return None

    new_direction = reflect(
        photon.direction,
        interaction.normal
    )

    photon.position = (
        interaction.position
        +
        new_direction * EPSILON
    )

    photon.direction = new_direction

    photon.reflections += 1

    return interaction