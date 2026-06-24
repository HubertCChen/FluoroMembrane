import math


def distance_to_plane(
    position,
    direction,
    plane_coordinate,
    axis
):
    """
    Calculate distance to a plane.

    axis:
        'x'
        'y'
        'z'
    """

    direction_component = getattr(
        direction,
        axis
    )

    if abs(direction_component) < 1e-12:
        return math.inf

    position_component = getattr(
        position,
        axis
    )

    distance = (
        plane_coordinate
        -
        position_component
    ) / direction_component

    if distance <= 0:
        return math.inf

    return distance