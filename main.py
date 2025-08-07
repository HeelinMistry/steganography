from utils.image_loader import load_image, save_image
from utils.encryption import generate_key, encrypt_message, decrypt_message
from steganography.lsb_image import LSBImageSteganography
from steganalysis.chi_square import chi_square_test
from steganalysis.image_diff import compare_images
from steganalysis.rs_analysis import rs_analysis

# 1. Load the image
carrier_img = load_image('data/example.png')

# 2. Encrypt the message
key = generate_key()
message = "This is a top secret message."
encrypted = encrypt_message(message, key)

# 3. Encode it
stego = LSBImageSteganography()
encoded_img = stego.encode(carrier_img, encrypted)
save_image(encoded_img, 'output/encoded.png')

# 4. Decode it
loaded_stego_img = load_image('output/encoded.png')
extracted = stego.decode(loaded_stego_img)

# 5. Decrypt
decrypted = decrypt_message(extracted, key)
print("Recovered message:", decrypted)

print("\nComparing original and stego image...")
compare_images(carrier_img, encoded_img, show_diff=False, diff_output_path="output/diff.png")

print("\nRunning chi-square test on stego image...")
chi_square_test(encoded_img)

print("\nRunning RS analysis on stego image...")
rs_analysis(encoded_img)
