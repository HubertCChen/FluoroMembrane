from dataclasses import dataclass

from core.vector import Vector


@dataclass
class PhotonResult:

    photon_id: int

    entry_position: Vector

    entry_direction: Vector

    final_position: Vector

    final_direction: Vector

    final_state: str

    travel_distance: float

    reflections: int

    scatterings: int

    absorptions: int

    reemissions: int