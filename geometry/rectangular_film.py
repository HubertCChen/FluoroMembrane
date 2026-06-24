from geometry.geometry import Geometry

from geometry.boundary import (
    distance_to_plane
)


class RectangularFilm(Geometry):

    def __init__(
        self,
        width,
        length,
        thickness,
        refractive_index
    ):

        self.width = width
        self.length = length
        self.thickness = thickness

        self.refractive_index = refractive_index

    def contains(self, position):

        return (
            0 <= position.x <= self.width
            and
            0 <= position.y <= self.length
            and
            0 <= position.z <= self.thickness
        )

    def nearest_boundary_distance(
        self,
        position,
        direction
    ):

        candidates = [

            (
                distance_to_plane(
                    position,
                    direction,
                    0,
                    "x"
                ),
                "X_MIN"
            ),

            (
                distance_to_plane(
                    position,
                    direction,
                    self.width,
                    "x"
                ),
                "X_MAX"
            ),

            (
                distance_to_plane(
                    position,
                    direction,
                    0,
                    "y"
                ),
                "Y_MIN"
            ),

            (
                distance_to_plane(
                    position,
                    direction,
                    self.length,
                    "y"
                ),
                "Y_MAX"
            ),

            (
                distance_to_plane(
                    position,
                    direction,
                    0,
                    "z"
                ),
                "BOTTOM"
            ),

            (
                distance_to_plane(
                    position,
                    direction,
                    self.thickness,
                    "z"
                ),
                "TOP"
            )

        ]

        return min(
            candidates,
            key=lambda item: item[0]
        )

