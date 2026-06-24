from dataclasses import dataclass

from core.vector import Vector


@dataclass
class PhotonEvent:

    event_number: int

    event_type: str

    position: Vector

    distance: float

    surface: str | None = None