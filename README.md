# Stegenography-Tool

## Overview
This project is a comprehensive GUI-based steganography tool built in Python. It allows users to securely hide and extract data using various steganographic techniques:

- Image to Text Steganography
- Image to Image Steganography
- Audio to Text Steganography
  
Users can encode (hide) or decode (extract) data with optional password protection (for text-in-image), and interact with a user-friendly interface designed using Tkinter.


## Features
- Encode and decode secret messages in PNG/BMP images
- Hide one image inside another image
- Embed and extract secret text from WAV audio files
- Password support for image-text steganography (optional)
- Intuitive GUI that dynamically updates based on user input selections


## Technologies Used
- Python 3.x
- Tkinter (GUI)
- wave (for audio handling)
- Custom `stegano.py` module for core logic


## Setup Instructions

### Prerequisites
- Python 3.x (recommended: Python 3.8+)

### Installation
1. Clone the repository:

```bash
git clone https://github.com/your-username/steganography-tool.git
cd steganography-tool
```

2. Install required libraries:

```bash
pip install pillow numpy
```


## Running the Application

```bash
python3 gui_lsb.py
```


## File Structure

```bash
├── gui_lsb.py            # Main GUI interface
├── stegano.py            # Core encoding/decoding logic
├── audio_output.wav      # Sample audio output (if generated)
├── secure_output.png     # Sample image output (if generated)
├── extracted_secret.png  # Image extracted from image (if generated)
├── README.md             # Project documentation
```


## Usage

1.Launch the application.

2.Select the type of steganography (Image → Text, Image → Image, Audio → Text).

3.Choose whether to encode or decode.

4.Fill in the prompted fields such as image path, message, audio file, or password.

5.Click on Perform Operation.

6.Output status and results will appear at the bottom. Decoded messages will appear in bold.


## Notes

-Only .png and .bmp files are supported for image operations.
-Audio files must be in .wav format (16-bit PCM).
-For image-in-image steganography, the secret image should be smaller than the cover image.

## License

This project is licensed under the MIT License.




