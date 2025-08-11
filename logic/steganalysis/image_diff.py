from PIL import Image, ImageChops
import numpy as np

def compare_images(original: Image.Image, modified: Image.Image, show_diff=False, diff_output_path=None):
    """
    Compare two images and return pixel difference count.
    Optionally show/save the visual difference.
    """
    original = original.convert("RGB")
    modified = modified.convert("RGB")

    if original.size != modified.size:
        raise ValueError("Images must be the same size to compare.")

    orig_data = np.array(original)
    mod_data = np.array(modified)

    diff_pixels = np.sum(orig_data != mod_data)
    total_pixels = orig_data.size
    percent_changed = (diff_pixels / total_pixels) * 100

    print("🔍 Image Comparison Result:")
    print(f"  - Total pixels: {total_pixels}")
    print(f"  - Pixels changed: {diff_pixels}")
    print(f"  - Percentage changed: {percent_changed:.4f}%")

    if show_diff or diff_output_path:
        # Show or save a visual diff image (highlight differences)
        diff_img = ImageChops.difference(original, modified)
        if show_diff:
            diff_img.show()
        if diff_output_path:
            diff_img.save(diff_output_path)
            print(f"🖼️  Diff image saved to: {diff_output_path}")

    return diff_pixels, percent_changed
