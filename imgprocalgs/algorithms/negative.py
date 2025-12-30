import argparse

from imgprocalgs.algorithms.base import BaseImageAlgorithm
from imgprocalgs.algorithms.utilities import Image, create_empty_image


class NegativeAlgorithm(BaseImageAlgorithm):
    """
    Converts an image into its negative.
    """

    def process(self):
        image = Image(self.image_path)
        width, height = image.get_size()

        output = create_empty_image(width, height)
        output_pixels = output.load()

        for x in range(width):
            for y in range(height):
                red, green, blue = image.pixels[x, y]
                output_pixels[x, y] = (
                    255 - red,
                    255 - green,
                    255 - blue
                )

        self.result = output


def parse_args():
    parser = argparse.ArgumentParser(description="Negative algorithm")
    parser.add_argument("--src", type=str, help="Source file path.")
    parser.add_argument("--dest", type=str, help="Destination file path.")
    return parser.parse_args()


def main():
    args = parse_args()
    algo = NegativeAlgorithm(args.src)
    algo.process()
    algo.result.save(args.dest)
