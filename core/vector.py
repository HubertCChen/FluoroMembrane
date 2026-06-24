from dataclasses import dataclass
import math


@dataclass
class Vector:

    x: float
    y: float
    z: float

    def magnitude(self):
        return math.sqrt(
            self.x**2 +
            self.y**2 +
            self.z**2
        )

    def normalize(self):

        mag = self.magnitude()

        if mag == 0:
            raise ValueError("Cannot normalize zero vector")

        return Vector(
            self.x / mag,
            self.y / mag,
            self.z / mag
        )

    def dot(self, other):

        return (
            self.x * other.x +
            self.y * other.y +
            self.z * other.z
        )

    def __add__(self, other):

        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):

        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, scalar):

        return Vector(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    def __rmul__(self, scalar):

        return self.__mul__(scalar)