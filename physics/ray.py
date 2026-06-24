from core.vector import Vector


def intersection_point(
    position: Vector,
    direction: Vector,
    distance: float
):

    return (
        position
        +
        direction * distance
    )