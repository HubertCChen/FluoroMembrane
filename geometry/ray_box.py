from geometry.boundary import (
    distance_to_plane
)

from physics.ray import (
    intersection_point
)

from geometry.surface import (
    get_surface_normal
)

from core.interaction import (
    Interaction
)

from core.interaction_type import (
    InteractionType
)


def next_boundary_interaction(
    film,
    position,
    direction
):

    candidates = [

        ("X_MIN", 0, "x"),
        ("X_MAX", film.width, "x"),

        ("Y_MIN", 0, "y"),
        ("Y_MAX", film.length, "y"),

        ("BOTTOM", 0, "z"),
        ("TOP", film.thickness, "z")

    ]

    valid_hits = []

    for surface, plane_value, axis in candidates:

        distance = distance_to_plane(
            position,
            direction,
            plane_value,
            axis
        )

        if distance == float("inf"):
            continue

        point = intersection_point(
            position,
            direction,
            distance
        )

        if surface in ["TOP", "BOTTOM"]:

            if not (
                0 <= point.x <= film.width
                and
                0 <= point.y <= film.length
            ):
                continue

        elif surface in ["X_MIN", "X_MAX"]:

            if not (
                0 <= point.y <= film.length
                and
                0 <= point.z <= film.thickness
            ):
                continue

        elif surface in ["Y_MIN", "Y_MAX"]:

            if not (
                0 <= point.x <= film.width
                and
                0 <= point.z <= film.thickness
            ):
                continue

        valid_hits.append(

            Interaction(

                distance=distance,

                position=point,

                interaction_type=InteractionType.BOUNDARY

                surface=surface,

                normal=get_surface_normal(
                    surface
                )

            )

        )

    if len(valid_hits) == 0:

        return None

    return min(
        valid_hits,
        key=lambda hit: hit.distance
    )