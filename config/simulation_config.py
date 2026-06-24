from dataclasses import dataclass


@dataclass
class SimulationConfig:

    store_summary: bool = True

    store_photon: bool = False

    store_events: bool = False