# Image to Icon Converter

This Python script converts image files to icon files with multiple sizes.

## Requirements

- Python 3
- Pillow

## Installation

1. Clone this repository.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```
## Usage
Place your image files in the input directory.
Run the script:
```bash
python app.py
```
The script will convert all image files in the input directory to icons and save them in the output directory. The output icons will have the same base name as the input images, but with a .ico extension.

## Supported Image Formats
The script supports the following image formats:
- PNG
- JPEG
- TIFF
- BMP
- GIF

## Icon Sizes
The script generates icons with the following sizes:
- 16x16
- 32x32
- 48x48
- 64x64