from abc import ABC, abstractmethod

class SteganographyBase(ABC):

    @abstractmethod
    def encode(self, carrier, payload: bytes) -> any:
        pass

    @abstractmethod
    def decode(self, stego_carrier) -> bytes:
        pass
