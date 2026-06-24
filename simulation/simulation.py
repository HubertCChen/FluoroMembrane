from simulation.simulator import (
    run_photon
)


class Simulation:

    def __init__(

        self,

        source,

        film,

        material,

        observer
    ):

        self.source = source

        self.film = film

        self.material = material

        self.observer = observer

    def run(

        self,

        n_photons
    ):

        self.observer.begin()

        for _ in range(n_photons):

            photon = self.source.generate_photon()

            run_photon(

                photon,

                self.film,

                self.material,

                self.observer
            )

        self.observer.end()