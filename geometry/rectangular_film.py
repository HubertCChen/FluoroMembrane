from geometry.geometry import Geometry


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

    def classify_exit(self, position):

        if position.z < 0:
            return "BOTTOM_EXIT"

        if position.z > self.thickness:
            return "TOP_EXIT"

        return "EDGE_EXIT"