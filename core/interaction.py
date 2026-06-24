from dataclasses import dataclass

from core.vector import Vector

from core.interaction_type import (
    InteractionType
)


@dataclass
class Interaction:

    distance: float

    position: Vector

    interaction_type: InteractionType

    surface: str | None = None

    normal: Vector | None = None