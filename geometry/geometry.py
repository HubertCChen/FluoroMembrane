from abc import ABC, abstractmethod


class Geometry(ABC):

    @abstractmethod
    def contains(self, position):
        pass