from PIL import Image
import os
import math


def adjust_aspect_ratio(input_directory, output_directory, aspect_width, aspect_height):
    aspect_ratio = aspect_width / aspect_height
    for file in os.listdir(input_directory):
        filename, extension = os.path.splitext(file)
        image = Image.open(f"{input_directory}/{file}")

        image_width, image_height = image.size
        image_ratio = image_width / image_height
        error = math.fabs(image_ratio - aspect_ratio) / aspect_ratio
        adjusted_width = image_width
        adjusted_height = image_height
        x_adjustment = 0
        y_adjustment = 0

        if error <= 0.01:
            adjusted_width = image_width
            adjusted_height = image_height
            x_adjustment = 0
            y_adjustment = 0

        if image_ratio < aspect_ratio:
            adjusted_width = aspect_ratio * image_height
            x_adjustment = (adjusted_width - image_width) / 2
            y_adjustment = 0

        elif image_ratio > aspect_ratio:
            adjusted_height = image_width / aspect_ratio
            y_adjustment = (adjusted_height - image_height) / 2
            x_adjustment = 0

        adjusted_width = int(adjusted_width)
        adjusted_height = int(adjusted_height)
        x_adjustment = int(x_adjustment)
        y_adjustment = int(y_adjustment)

        canvass = Image.new('RGB', (adjusted_width, adjusted_height), "#000000")
        canvass.paste(image, (x_adjustment, y_adjustment))
        output_filename = f"{output_directory}/{file}"
        canvass.save(output_filename)
        print(f"[/] Successfully exported to {output_filename}")


if __name__ == "__main__":
    directory = "images/projects_raw"
    output_directory = "images/projects"
    aspect_ratio = (680, 460)
    aspect_width, aspect_height = aspect_ratio
    adjust_aspect_ratio(input_directory=directory, output_directory=output_directory, aspect_width=aspect_width, aspect_height=aspect_height)