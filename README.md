# Stegenography-Tool

Overview

This project is a comprehensive GUI-based steganography tool built in Python. It allows users to securely hide and extract data using various steganographic techniques:

Image to Text Steganography

Image to Image Steganography

Audio to Text Steganography

Users can encode (hide) or decode (extract) data with optional password protection (for text-in-image), and interact with a user-friendly interface designed using Tkinter.

Features

Encode and decode secret messages in PNG/BMP images

Hide one image inside another image

Embed and extract secret text from WAV audio files

Password support for image-text steganography (optional)

Intuitive GUI that dynamically updates based on user input selections

Technologies Used

Python 3.x

Tkinter (GUI)

wave (for audio handling)

Custom stegano.py module for core logic

Setup Instructions

Prerequisites

Python 3.x (recommended: Python 3.8+)

Installation

Clone the repository:

git clone https://github.com/your-username/steganography-tool.git
cd steganography-tool

Install required libraries:

pip install pillow

(Optional) If using additional image/audio formats, install:

pip install numpy

Running the Application

python3 gui_lsb.py

File Structure

├── gui_lsb.py          # Main GUI interface
├── stegano.py          # Core encoding/decoding logic
├── audio_output.wav    # Sample output file (if generated)
├── secure_output.png   # Sample image output (if generated)
├── extracted_secret.png# Image extracted from image (if generated)
├── README.md           # Project documentation

Usage

Launch the application.

Select the type of steganography.

Choose whether to encode or decode.

The application will show the relevant inputs (e.g., image path, secret message, etc.)

Click on Perform Operation to complete the task.

Output status and results will be shown below the input area.

Notes

Only .png and .bmp files are supported for image operations.

Audio files must be in .wav format (16-bit PCM).

The secret image in image-in-image steganography should ideally be smaller than the cover image.

License

This project is licensed under the MIT License.

