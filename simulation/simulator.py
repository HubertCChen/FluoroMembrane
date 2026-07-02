from physics.next_interaction import (
    next_interaction
)

from physics.execute_interaction import (
    execute_interaction
)


def run_photon(

    photon,

    film,

    material,

    physics,

    observer,

    max_interactions=10000
):

    interaction_count = 0

    observer.initialize_photon(
        photon
    )

    while photon.alive:

        interaction = (

            next_interaction(

                photon,

                film,

                material,

                physics
            )
        )

        if interaction is None:

            photon.alive = False

            photon.final_state = "NO_INTERACTION"

            break

        execute_interaction(

            photon,

            interaction
        )

        observer.record_event(

            photon,

            interaction
        )

        interaction_count += 1

        if interaction_count >= max_interactions:

            photon.alive = False

            photon.final_state = "MAX_INTERACTIONS"

            break

    observer.finalize_photon(
        photon
    )

    return photon