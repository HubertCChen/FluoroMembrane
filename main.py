from core.vector import Vector

from geometry.rectangular_film import (
    RectangularFilm
)

film = RectangularFilm(
    width=0.210,
    length=0.297,
    thickness=0.0004,
    refractive_index=1.49
)

position = Vector(
    0.100,
    0.100,
    0.0002
)

direction = Vector(
    0,
    0,
    1
).normalize()

distance, surface = (
    film.nearest_boundary_distance(
        position,
        direction
    )
)

print(distance)
print(surface)