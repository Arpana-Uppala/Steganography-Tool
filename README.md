# SteganoTool

**SteganoTool** is a Python-based steganography application that enables users to securely embed and extract hidden information within images and audio files using a simple and intuitive graphical interface.

## Features

- Hide text in image (LSB steganography)
- Extract text from stego-image
- Hide one image inside another
- Extract hidden image from stego-image
- Hide text inside audio files
- Extract hidden text from audio files
- Clean and user-friendly GUI built with `tkinter`
- macOS `.app` standalone build (no need to install Python)

## File Structure

```
SteganoTool/
├── gui.py               # Main GUI entry pointee
├── stegano.py           # Core steganography logic (encode/decode)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── .gitignore           # Git ignore rules

```

## Dependencies

The following Python libraries are used in this project:

- `altgraph==0.17.4`
- `colorama==0.4.6`
- `crayons==0.4.0`
- `macholib==1.16.3`
- `modulegraph==0.19.6`
- `numpy==2.3.0`
- `opencv-python==4.11.0.86`
- `packaging==25.0`
- `piexif==1.1.3`
- `pillow==10.4.0`
- `py2app==0.28.8`
- `pycryptodome==3.23.0`
- `pydub==0.25.1`
- `pyinstaller==6.14.1`
- `pyinstaller-hooks-contrib==2025.5`
- `setuptools==80.9.0`
- `stegano==1.0.1`
- `tk==0.1.0`

These are automatically installed using the `requirements.txt`.

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
- tkinter and other libraries are bundled in the standalone `.app` build

## Download Pre-Built App

You can download the pre-built macOS `.app` version from the following link:

**[Download SteganoTool macOS Build](https://github.com/Arpana-Uppala/Steganography-Tool/releases/download/v1.0.0/SteganoTool.zip)**

## License

This project is released under the MIT License. See `LICENSE` for details.







