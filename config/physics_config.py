class PhysicsConfig:

    def __init__(

        self,

        # Enable / disable physics
        absorption=True,

        scattering=False,

        fluorescence=False,

        # Physics models
        boundary_model="mirror",

        scattering_model="isotropic"

    ):

        self.absorption = absorption

        self.scattering = scattering

        self.fluorescence = fluorescence

        self.boundary_model = boundary_model

        self.scattering_model = scattering_model