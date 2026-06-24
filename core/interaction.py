from dataclasses import dataclass

from core.vector import Vector


@dataclass
class Interaction:

    distance: float

    position: Vector

    interaction_type: str

    surface: str | None = None

    normal: Vector | None = None