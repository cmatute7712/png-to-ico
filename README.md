# Image to Icon Converter

This Python script converts image files to icon files with multiple sizes.

### Requirements

- Python 3
- Pillow

### Standard Installation

1. Clone this repository.
```bash
git clone https://github.com/cmatute7712/png-to-ico.git
```
2. CD to the new project folder

```bash
cd png-to-ico
```
3. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```
### Usage
1. Place your image files in the input directory.
2. Run the script:
```bash
python app.py
```

### Docker 
You can run this project with docker or docker-compose using the appropriate files in this repo.
1. Clone the repository and CD into the project folder as we would do for a normal install..
2. Place your image files to be converted into the input folder.
2. Either run the dockerfile or the docker-compose

```bash
docker build -t png-to-ico . && docker run png-to-ico
```
```bash
docker-compose up -d
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