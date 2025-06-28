# SteganoTool

**SteganoTool** is a cross-platform steganography application developed in Python. It allows users to securely embed and extract hidden messages and images within cover media such as images and audio files using an intuitive graphical interface built with Tkinter.

---

## Features

- Embed text within image files using Least Significant Bit (LSB) steganography
- Extract hidden text from images using AES-based optional password decryption
- Embed one image inside another using 4 MSB-to-LSB encoding
- Extract hidden images with automatic size detection
- Embed and extract text inside uncompressed `.wav` audio files
- Supports AES encryption for secure message protection
- Standalone GUI-based usage; no command line required
- Platform-independent: source code runs on any OS with Python 3.9+
- Standalone executables available for macOS and Windows

---


## File Structure

```
SteganoTool/
├── gui.py # Main GUI interface
├── stegano.py # Core steganography logic
├── README.md # Project documentation
```
---

## System Requirements

### General

- Python 3.9 or later
- Tkinter (included in Python standard distribution)
- pip (for dependency installation)

### macOS Build

- macOS Ventura, Monterey, or later (Intel or Apple Silicon)
- `pyinstaller` or `py2app`

### Windows Build

- Windows 10 or 11
- `pyinstaller`

---

## Dependencies

### Runtime Requirements

- `pillow==10.4.0`
- `pycryptodome==3.23.0`
- `pydub==0.25.1`
- `numpy==2.3.0`
- `opencv-python==4.11.0.86`
- `stegano==1.0.1`

Install all runtime requirements via:
  ```bash
  pip install -r requirements.txt
  ```

### macOS Packaging Requirements

- `py2app==0.28.8`
- `altgraph==0.17.4`
- `macholib==1.16.3`
- `modulegraph==0.19.6`
- `crayons==0.4.0`

### Windows Packaging Requirements

- `pyinstaller==6.14.1`
- `pyinstaller-hooks-contrib==2025.5`
- `colorama==0.4.6`
- `packaging==25.0`

## How to Use

### Running from Source

1. Ensure Python 3.9+ is installed.
2. Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  Run the GUI:

    ```bash
    python gui.py
    ```


---

## Building Standalone Application

### macOS (.app)

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
### Windows (.exe)
```bash
pip install pyinstaller
pyinstaller --windowed --onefile gui.py
```

Output: `dist/gui.exe`

Optionally rename:

```bash
ren dist\gui.exe SteganoTool.exe
```

Then double-click to run.

---

## Functional Limits and Recommendations

The tool has practical limits based on pixel capacity, audio frame count, and GUI responsiveness:

| Feature               | Limitations and Recommendations                                              |
|-----------------------|------------------------------------------------------------------------------|
| Text in Image         | Stores 1 bit per pixel (blue channel). Recommended image size: ≥ 632×632    |
|                       | for up to ~50,000 characters. Only PNG/BMP formats are supported.            |
| Image in Image        | Secret image must be smaller than cover image in width and height.           |
|                       | Uses 4 MSBs of each color channel.                                           |
| Text in Audio         | Only uncompressed `.wav` files supported. Requires ~400,000 audio frames     |
|                       | to store 50,000 characters (~9 seconds at 44.1 kHz mono).                    |
| Message Length        | Recommended maximum: 50,000 characters for all modes.                        |
| Password Length       | Maximum 256 characters (AES-256 key derived from SHA-256 hash).              |
| Audio File Size       | Recommended maximum: 500 MB (larger sizes possible but slower performance).  |

Encoding beyond these limits may result in slow execution, decoding failure, or corrupted outputs.

---

## Compatibility

- macOS Ventura, Monterey, Sonoma (Intel and Apple Silicon)
- Windows 10 and 11
- Python 3.9 and above
- Tkinter-based GUI works on all platforms

---

## Pre-Built Releases

Pre-built application binaries will be available on the [GitHub Releases page]((https://github.com/Arpana-Uppala/Steganography-Tool/releases)):

- **[Download SteganoTool macOS Build](https://github.com/Arpana-Uppala/Steganography-Tool/releases/tag/v1.0.0)**
 
- **[Download SteganoTool Windows Build](https://github.com/Arpana-Uppala/Steganography-Tool/releases/tag/v1.0)**
These can be used without installing Python or additional dependencies.

---


## License

This project is released under the MIT License. See `LICENSE` for details.







