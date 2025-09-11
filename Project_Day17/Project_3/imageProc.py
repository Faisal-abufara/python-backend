import os
from PIL import Image
import argparse


class ImageProcessor:
    def __init__(self, input_dir: str, output_dir: str):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.supported_extensions = (".jpg", ".jpeg", ".png")

    def ensure_output_dir(self):
        """Create output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def get_image_files(self) -> list:
        """Retrieve list of supported image files from input directory."""
        return [
            f
            for f in os.listdir(self.input_dir)
            if os.path.isfile(os.path.join(self.input_dir, f))
            and f.lower().endswith(self.supported_extensions)
        ]

    def resize_image(self, image: Image.Image, width: int, height: int) -> Image.Image:
        """Resize image to specified dimensions."""
        return image.resize((width, height), Image.Resampling.LANCZOS)

    def convert_to_grayscale(self, image: Image.Image) -> Image.Image:
        """Convert image to grayscale."""
        return image.convert("L")

    def rotate_image(self, image: Image.Image, angle: float) -> Image.Image:
        """Rotate image by specified angle."""
        return image.rotate(angle, expand=True)

    def process_images(
        self, resize: tuple = None, grayscale: bool = False, rotate: float = None
    ):
        """Process all images in input directory with specified transformations."""
        self.ensure_output_dir()
        image_files = self.get_image_files()

        if not image_files:
            print("No supported image files found in input directory.")
            return

        for filename in image_files:
            try:
                input_path = os.path.join(self.input_dir, filename)
                output_path = os.path.join(self.output_dir, f"processed_{filename}")

                with Image.open(input_path) as img:
                    # Apply transformations
                    if resize:
                        img = self.resize_image(img, resize[0], resize[1])
                    if grayscale:
                        img = self.convert_to_grayscale(img)
                    if rotate is not None:
                        img = self.rotate_image(img, rotate)

                    # Save processed image
                    img.save(output_path)
                    print(f"Processed: {filename} -> {output_path}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")


def main():
    parser = argparse.ArgumentParser(description="Batch image processing tool")
    parser.add_argument("input_dir", help="Input directory containing images")
    parser.add_argument("output_dir", help="Output directory for processed images")
    parser.add_argument(
        "--resize",
        nargs=2,
        type=int,
        metavar=("WIDTH", "HEIGHT"),
        help="Resize images to WIDTH x HEIGHT",
    )
    parser.add_argument(
        "--grayscale", action="store_true", help="Convert images to grayscale"
    )
    parser.add_argument("--rotate", type=float, help="Rotate images by ANGLE degrees")

    args = parser.parse_args()

    processor = ImageProcessor(args.input_dir, args.output_dir)

    # Prepare resize dimensions if provided
    resize_dims = (args.resize[0], args.resize[1]) if args.resize else None

    # Process images with specified transformations
    processor.process_images(
        resize=resize_dims, grayscale=args.grayscale, rotate=args.rotate
    )


if __name__ == "__main__":
    main()