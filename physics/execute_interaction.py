from physics.reflection import (
    reflect
)

from core.interaction_type import (
    InteractionType
)


EPSILON = 1e-12


def execute_interaction(
    photon,
    interaction
):
    """
    Execute the physical interaction.

    This function ONLY changes the physical state of the photon.
    It does NOT record events or save any output.
    """

    # Add travelled distance
    photon.travel_distance += interaction.distance

    # ==========================
    # Absorption
    # ==========================
    if interaction.interaction_type == InteractionType.ABSORPTION:

        photon.position = interaction.position

        photon.alive = False

        photon.final_state = "ABSORBED"

        photon.absorptions += 1

        return

    # ==========================
    # Boundary Reflection
    # ==========================
    if interaction.interaction_type == InteractionType.BOUNDARY:

        new_direction = reflect(
            photon.direction,
            interaction.normal
        )

        photon.position = (
            interaction.position
            + new_direction * EPSILON
        )

        photon.direction = new_direction

        photon.reflections += 1

        return