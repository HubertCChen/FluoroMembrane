from core.vector import Vector


def get_surface_normal(
    surface
):

    normals = {

        "X_MIN": Vector(
            -1,
            0,
            0
        ),

        "X_MAX": Vector(
            1,
            0,
            0
        ),

        "Y_MIN": Vector(
            0,
            -1,
            0
        ),

        "Y_MAX": Vector(
            0,
            1,
            0
        ),

        "BOTTOM": Vector(
            0,
            0,
            -1
        ),

        "TOP": Vector(
            0,
            0,
            1
        )
    }

    return normals[surface]