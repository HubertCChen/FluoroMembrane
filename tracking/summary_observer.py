from tracking.base_observer import (
    BaseObserver
)


class SummaryObserver(BaseObserver):

    def __init__(self):

        self.total = 0

        self.absorbed = 0

        self.edge_exit = 0

        self.top_exit = 0

        self.bottom_exit = 0

    def initialize_photon(
        self,
        photon
    ):

        self.total += 1

    def record_event(
        self,
        photon,
        interaction
    ):

        pass

    def finalize_photon(
        self,
        photon
    ):

        if photon.final_state == "ABSORBED":

            self.absorbed += 1

        elif photon.final_state == "EDGE_EXIT":

            self.edge_exit += 1

        elif photon.final_state == "TOP_EXIT":

            self.top_exit += 1

        elif photon.final_state == "BOTTOM_EXIT":

            self.bottom_exit += 1