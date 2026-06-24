from physics.bounce import bounce


def run_photon(
    photon,
    film,
    max_bounces=1000
):

    while photon.alive:

        interaction = bounce(
            photon,
            film
        )

        if interaction is None:

            photon.alive = False

            photon.final_state = (
                "NO_INTERACTION"
            )

            break

        if photon.reflections >= max_bounces:

            photon.alive = False

            photon.final_state = (
                "MAX_BOUNCES"
            )

            break

    return photon