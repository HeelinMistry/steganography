import argparse
from utils.image_loader import load_image, save_image
from utils.encryption import generate_key, encrypt_message, decrypt_message
from steganography.lsb_image import LSBImageSteganography
from steganalysis.chi_square import chi_square_test
from steganalysis.image_diff import compare_images
from steganalysis.rs_analysis import rs_analysis

def main():
    parser = argparse.ArgumentParser(description="LSB Steganography CLI tool")
    parser.add_argument('--carrier', required=True, help='Path to carrier image')
    parser.add_argument('--secret', help='Path to secret file (to hide)')
    parser.add_argument('--output_img', default='output/encoded.png', help='Path to save encoded image')
    parser.add_argument('--output_secret', default='output/recovered_secret.txt', help='Path to save recovered secret')
    parser.add_argument('--diff_output', default='output/diff.png', help='Path to save image diff')
    parser.add_argument('--decode_only', action='store_true', help='Only decode from existing stego image')
    args = parser.parse_args()

    stego = LSBImageSteganography()

    if args.decode_only:
        # Just decode from stego image
        stego_img = load_image(args.carrier)
        extracted = stego.decode(stego_img)
        with open(args.output_secret, "wb") as f:
            f.write(extracted)
        print(f"Secret extracted to {args.output_secret}")
    else:
        # Full encode/decode workflow
        carrier_img = load_image(args.carrier)
        with open(args.secret, "rb") as f:
            secret_bytes = f.read()

        # Encode
        encoded_img = stego.encode(carrier_img, secret_bytes)
        save_image(encoded_img, args.output_img)
        print(f"Encoded image saved to {args.output_img}")

        # Decode
        loaded_stego_img = load_image(args.output_img)
        extracted = stego.decode(loaded_stego_img)
        with open(args.output_secret, "wb") as f:
            f.write(extracted)
        print(f"Recovered secret saved to {args.output_secret}")

        # Analysis
        print("\nComparing original and stego image...")
        compare_images(carrier_img, encoded_img, show_diff=False, diff_output_path=args.diff_output)

        print("\nRunning chi-square test on stego image...")
        chi_square_test(encoded_img)

        print("\nRunning RS analysis on stego image...")
        rs_analysis(encoded_img)

if __name__ == "__main__":
    main()

# python stego_cli.py --carrier data/example.png --secret data/secret.txt

# python stego_cli.py --carrier output/encoded.png --decode_only
