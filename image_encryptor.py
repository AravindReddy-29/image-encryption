from PIL import Image

def encrypt_image(input_image, output_image, key):
    image = Image.open(input_image)
    pixels = image.load()

    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_image)
    print("Image Encrypted Successfully!")


def decrypt_image(input_image, output_image, key):
    image = Image.open(input_image)
    pixels = image.load()

    width, height = image.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            pixels[i, j] = (r, g, b)

    image.save(output_image)
    print("Image Decrypted Successfully!")


print("===== IMAGE ENCRYPTION TOOL =====")

choice = input("Enter Encrypt(E) or Decrypt(D): ").upper()

key = int(input("Enter Secret Key: "))

if choice == "E":
    encrypt_image("input.jpg", "encrypted.png", key)

elif choice == "D":
    decrypt_image("encrypted.png", "decrypted.png", key)

else:
    print("Invalid Choice")