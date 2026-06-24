from enum import Enum


class InteractionType(Enum):

    BOUNDARY = "BOUNDARY"

    ABSORPTION = "ABSORPTION"

    SCATTERING = "SCATTERING"

    FLUORESCENCE = "FLUORESCENCE"

    DETECTOR = "DETECTOR"