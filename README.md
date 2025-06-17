# SteganoTool

**SteganoTool** is a Python-based steganography application featuring a user-friendly GUI built with `tkinter`. This tool allows users to securely embed and extract hidden data in digital media using multiple steganographic techniques.

## Overview

The application supports:

- Hiding and extracting **text messages** inside images
- Embedding and retrieving **images within images**
- Encoding and decoding **audio files (WAV format) within images**

The tool is developed to demonstrate secure and covert communication through steganography and provides a simplified interface suitable for educational and personal use.

## Features

- Graphical User Interface using `tkinter`
- Supports commonly used image formats (`.png`, `.jpg`, `.bmp`)
- Supports WAV audio file embedding
- Modular code structure for easy maintenance and extension
- Compatible with macOS systems
- Packaged as a standalone application using PyInstaller

## Requirements

To run the application from source, ensure the following Python packages are installed:

- Pillow
- OpenCV (`opencv-python`)
- NumPy

You can install them using the following command:

```bash
pip3 install -r requirements.txt
```

## File Structure

```
SteganoTool/
├── gui.py               # Main GUI entry point
├── stegano.py           # Core steganography logic (encode/decode)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules
└── dist/                # (Optional) Folder containing built application
```

## How to Use

### Run from Source

1. Ensure Python 3.x is installed.
2. Install required packages:

    ```bash
    pip3 install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python3 gui.py
    ```

### Build Standalone Application (macOS)

To build the `.app` file using PyInstaller:

1. Install PyInstaller:

    ```bash
    pip3 install pyinstaller
    ```

2. Create the standalone app:

    ```bash
    pyinstaller --windowed --onefile gui.py
    ```

3. Navigate to the `dist/` directory:

    ```bash
    ./dist/gui
    ```

To rename the application:

```bash
mv dist/gui dist/SteganoTool
./dist/SteganoTool
```

If you prefer a `.app` bundle:

```bash
pyinstaller --windowed gui.py
open dist/gui.app
```

## Compatibility

- Developed and tested on macOS (Intel and Apple Silicon)
- Compatible with Python 3.9 and above
- tkinter and other core libraries are standard in most Python installations

## Limitations

- Audio steganography currently supports only uncompressed `.wav` format
- Large file embedding may increase processing time
- GUI optimized for medium-resolution screens (recommended 13" and above)

## Contributing

This project is currently a part of an academic internship and is not open to public contributions. However, if you encounter issues or would like to suggest enhancements, feel free to open an issue.

## License

This project is released for educational and research purposes. This project is licensed under the MIT License.

## Download

To download the compiled `.app` version for macOS, use the link below:  

https://drive.google.com/drive/folders/1oZDonjNfxDrQ6d0zj6Q_SOrKLqhECtxq






