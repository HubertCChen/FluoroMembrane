from dataclasses import dataclass

from core.vector import Vector


@dataclass
class Photon:

    photon_id: int

    position: Vector
    direction: Vector

    wavelength: float

    alive: bool = True

    travel_distance: float = 0.0

    reflections: int = 0
    scatterings: int = 0
    absorptions: int = 0
    reemissions: int = 0

    final_state: str | None = None

    history: list | None = None

    initial_position: Vector | None = None
    initial_direction: Vector | None = None