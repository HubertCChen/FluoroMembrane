from core.vector import Vector


def reflect(
    incident: Vector,
    normal: Vector
):

    dot_product = incident.dot(
        normal
    )

    reflected = (
        incident
        -
        normal * (
            2 * dot_product
        )
    )

    return reflected.normalize()