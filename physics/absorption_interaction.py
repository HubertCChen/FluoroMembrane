from physics.absorption import (
    sample_absorption_distance
)

from physics.ray import (
    intersection_point
)

from core.interaction import (
    Interaction
)

from core.interaction_type import (
    InteractionType
)


def next_absorption_interaction(
    photon,
    material
):

    distance = (
        sample_absorption_distance(
            material.mu_abs
        )
    )

    position = (
        intersection_point(
            photon.position,
            photon.direction,
            distance
        )
    )

    return Interaction(

        distance=distance,

        position=position,

        interaction_type=
        InteractionType.ABSORPTION

    )