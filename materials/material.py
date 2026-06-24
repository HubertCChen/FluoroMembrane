from dataclasses import dataclass


@dataclass
class Material:

    refractive_index: float

    mu_abs: float

    mu_scat: float