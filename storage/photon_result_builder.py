from core.photon_result import (
    PhotonResult
)


def build_photon_result(
    photon
):

    return PhotonResult(

        photon_id=
        photon.photon_id,

        entry_position=
        photon.initial_position,

        entry_direction=
        photon.initial_direction,

        final_position=
        photon.position,

        final_direction=
        photon.direction,

        final_state=
        photon.final_state,

        travel_distance=
        photon.travel_distance,

        reflections=
        photon.reflections,

        scatterings=
        photon.scatterings,

        absorptions=
        photon.absorptions,

        reemissions=
        photon.reemissions
    )