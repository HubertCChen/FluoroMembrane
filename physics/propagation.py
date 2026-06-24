from core.photon import Photon


def propagate(
    photon: Photon,
    distance: float
):
    """
    Move photon along current direction.

    distance in meters.
    """

    photon.position = (
        photon.position
        +
        photon.direction * distance
    )

    photon.travel_distance += distance