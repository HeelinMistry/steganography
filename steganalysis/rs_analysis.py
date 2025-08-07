from PIL import Image
import numpy as np

def calculate_group_smoothness(group):
    group = group.astype(np.int16)  # Avoid overflow by converting to signed type
    return sum(abs(group[i] - group[i + 1]) for i in range(len(group) - 1))


def flip_lsb(pixels):
    return pixels ^ 1

def rs_analysis(image: Image.Image, group_size=3):
    img = image.convert("L")  # Grayscale
    pixels = np.array(img).flatten()

    R = S = R_flipped = S_flipped = 0

    for i in range(0, len(pixels) - group_size + 1, group_size):
        group = pixels[i:i+group_size]
        smoothness = calculate_group_smoothness(group)

        if smoothness > calculate_group_smoothness(flip_lsb(group)):
            R += 1
        else:
            S += 1

        flipped_group = flip_lsb(group)
        smoothness_flipped = calculate_group_smoothness(flipped_group)

        if smoothness_flipped > calculate_group_smoothness(flip_lsb(flipped_group)):
            R_flipped += 1
        else:
            S_flipped += 1

    total = R + S
    total_flipped = R_flipped + S_flipped

    print("🔬 RS Analysis Result:")
    print(f"  - Regular groups (R):        {R}")
    print(f"  - Singular groups (S):       {S}")
    print(f"  - Flipped Regular (R’):      {R_flipped}")
    print(f"  - Flipped Singular (S’):     {S_flipped}")
    print(f"  - R/S Ratio:                 {R / S if S != 0 else float('inf'):.4f}")
    print(f"  - R’/S’ Ratio:               {R_flipped / S_flipped if S_flipped != 0 else float('inf'):.4f}")

    # In natural images: R/S ≈ R'/S'
    # In stego images: R/S > R'/S' or reversed

    if abs((R / S if S != 0 else 0) - (R_flipped / S_flipped if S_flipped != 0 else 0)) > 0.2:
        print("❗ RS test suggests possible hidden data.")
    else:
        print("✅ RS test suggests natural image.")

    return R, S, R_flipped, S_flipped
