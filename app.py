import os
from PIL import Image

def convert_image_to_icon(image_path, icon_sizes, output_path):
    """Converts an image to an icon with multiple sizes.

    Args:
        image_path (str): The path to the image file.
        icon_sizes (list): A list of tuples representing the sizes for the icon.
        output_path (str): The path to save the icon file.
    """
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"No such file: '{image_path}'")

    img = Image.open(image_path)
    img.save(output_path, sizes=icon_sizes)

if __name__ == "__main__":
    input_folder = 'input'
    output_folder = 'output'
    icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]

    # Check if there are any image files
    if not image_files:
        raise ValueError("No image files found in the input directory.")

    # Loop over all image files
    for filename in image_files:
        input_path = os.path.join(input_folder, filename)
        base_name = os.path.splitext(filename)[0]  # get the base name of the file
        output_path = os.path.join(output_folder, f'{base_name}.ico')
        convert_image_to_icon(input_path, icon_sizes, output_path)