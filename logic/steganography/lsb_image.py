from steganography.base import SteganographyBase
from PIL import Image
import numpy as np


class LSBImageSteganography(SteganographyBase):

    def encode(self, carrier: Image.Image, payload: bytes) -> Image.Image:
        binary_data = ''.join(format(byte, '08b') for byte in payload) + '1111111111111110'  # EOF marker
        data_len = len(binary_data)
        carrier = carrier.convert("RGB")
        pixels = np.array(carrier)
        flat = pixels.flatten()

        if data_len > len(flat):
            raise ValueError("Payload too large for image.")

        for i in range(data_len):
            flat[i] = (flat[i] & 0xFE) | int(binary_data[i])

        pixels = flat.reshape(pixels.shape)
        return Image.fromarray(pixels)

    def decode(self, stego_carrier: Image.Image) -> bytes:
        stego_carrier = stego_carrier.convert("RGB")
        pixels = np.array(stego_carrier).flatten()
        bits = [str(p & 1) for p in pixels]
        binary_string = ''.join(bits)
        eof_index = binary_string.find('1111111111111110')

        if eof_index == -1:
            raise ValueError("EOF marker not found. Message may be corrupted or missing.")

        binary_string = binary_string[:eof_index]
        byte_chunks = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
        return bytes([int(b, 2) for b in byte_chunks])
