from PIL import Image
from Crypto.Cipher import AES
import hashlib
import base64

# --- Encryption Helpers ---

def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def encrypt_message(message, password):
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(pad(message).encode())
    return base64.b64encode(encrypted).decode()

def decrypt_message(enc_message, password):
    key = hashlib.sha256(password.encode()).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(enc_message))
    return decrypted.decode().rstrip()

# --- LSB Encoding ---

def to_bin(data):
    return ''.join(format(ord(i), '08b') for i in data)

def from_bin(binary_data):
    chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(chars)

def encode_lsb(image_path, secret_message, password, output_path):
    encrypted = encrypt_message(secret_message, password) + '####'  # marker
    binary = to_bin(encrypted)

    img = Image.open(image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = img.load()
    w, h = img.size

    idx = 0
    for y in range(h):
        for x in range(w):
            if idx < len(binary):
                r, g, b = pixels[x, y]
                b = (b & ~1) | int(binary[idx])
                pixels[x, y] = (r, g, b)
                idx += 1
            else:
                break
    img.save(output_path)
    print("Encrypted message hidden successfully.")

def decode_lsb(image_path, password):
    img = Image.open(image_path)
    pixels = img.load()
    w, h = img.size

    binary = ''
    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            binary += str(b & 1)

    message = from_bin(binary)
    message = message.split('####')[0]  # remove marker
    try:
        return decrypt_message(message, password)
    except:
        return "Incorrect password or corrupted data."
    
def encode_image_in_image(cover_img_path, secret_img_path, output_path):
    cover = Image.open(cover_img_path).convert('RGB')
    secret = Image.open(secret_img_path).convert('RGB')

    if secret.size[0] > cover.size[0] or secret.size[1] > cover.size[1]:
        raise ValueError("Secret image must be smaller than cover image")

    cover_pixels = cover.load()
    secret_pixels = secret.load()

    for y in range(secret.size[1]):
        for x in range(secret.size[0]):
            r_s, g_s, b_s = secret_pixels[x, y]
            r_c, g_c, b_c = cover_pixels[x, y]

            # Store 2 MSB of secret pixel into LSB of cover pixel
            r = (r_c & 0b11111100) | (r_s >> 6)
            g = (g_c & 0b11111100) | (g_s >> 6)
            b = (b_c & 0b11111100) | (b_s >> 6)

            cover_pixels[x, y] = (r, g, b)

    cover.save(output_path)
    print("✅ Image hidden successfully in", output_path)

def decode_image_from_image(stego_image_path, secret_size, output_path):
    stego = Image.open(stego_image_path).convert('RGB')
    pixels = stego.load()

    w, h = secret_size
    secret = Image.new('RGB', (w, h))
    secret_pixels = secret.load()

    for y in range(h):
        for x in range(w):
            r, g, b = pixels[x, y]
            r_s = (r & 0b00000011) << 6
            g_s = (g & 0b00000011) << 6
            b_s = (b & 0b00000011) << 6
            secret_pixels[x, y] = (r_s, g_s, b_s)

    secret.save(output_path)
    print("Secret image extracted as", output_path)

import wave

def encode_audio(audio_in_path, message, output_path):
    message += '###'  # Delimiter
    message_bits = ''.join([format(ord(c), '08b') for c in message])

    with wave.open(audio_in_path, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))
        if len(message_bits) > len(frames):
            raise ValueError("Message too long for this audio")

        for i, bit in enumerate(message_bits):
            frames[i] = (frames[i] & 254) | int(bit)

        with wave.open(output_path, 'wb') as out_audio:
            out_audio.setparams(audio.getparams())
            out_audio.writeframes(bytes(frames))

def decode_audio(audio_path):
    with wave.open(audio_path, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))
        bits = [str(frame & 1) for frame in frames]
        bytes_data = [bits[i:i+8] for i in range(0, len(bits), 8)]

        message = ''
        for byte in bytes_data:
            char = chr(int(''.join(byte), 2))
            message += char
            if message.endswith('###'):
                return message[:-3]
    return ""


