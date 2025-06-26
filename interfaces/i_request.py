from abc import ABC, abstractmethod

class IRequest(ABC):
    @abstractmethod
    def request(self):
        pass