from PIL import Image
import numpy as np
from scipy.stats import chisquare

def chi_square_test(image: Image.Image, verbose=True):
    """
    Perform Chi-Square Test to check for steganographic modification in LSBs.
    """
    image = image.convert("RGB")
    data = np.array(image).flatten()

    # Count frequencies of LSBs: 0 and 1
    lsb_counts = [0, 0]
    for value in data:
        lsb_counts[value & 1] += 1

    # Perform Chi-Square Test
    stat, p_value = chisquare(lsb_counts)

    if verbose:
        print("🧪 Chi-Square Test Result:")
        print(f"  - LSB counts: 0s = {lsb_counts[0]}, 1s = {lsb_counts[1]}")
        print(f"  - Chi-square statistic: {stat:.4f}")
        print(f"  - p-value: {p_value:.4f}")
        if p_value < 0.05:
            print("❗ Suspicious: image may be modified.")
        else:
            print("✅ Likely clean (natural image).")

    return stat, p_value
