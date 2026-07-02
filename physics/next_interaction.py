from geometry.ray_box import (
    next_boundary_interaction
)

from physics.absorption_interaction import (
    next_absorption_interaction
)


def next_interaction(

    photon,

    film,

    material,

    physics
):

    interactions = []

    #
    # Boundary
    #

    boundary = (

        next_boundary_interaction(

            film,

            photon.position,

            photon.direction
        )
    )

    if boundary is not None:

        interactions.append(
            boundary
        )

    #
    # Absorption
    #

    if physics.absorption:

        absorption = (

            next_absorption_interaction(

                photon,

                material
            )
        )

        if absorption is not None:

            interactions.append(
                absorption
            )

    #
    # Future interactions
    #

    if physics.scattering:

        pass

    if physics.fluorescence:

        pass

    #
    # No interactions
    #

    if len(interactions) == 0:

        return None

    #
    # Return nearest interaction
    #

    return min(

        interactions,

        key=lambda x: x.distance
    )