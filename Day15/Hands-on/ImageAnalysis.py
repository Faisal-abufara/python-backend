from PIL import Image, ImageFilter
import os

# Check if the file exists (should print True)
print("Exists:", os.path.exists("Defjam.png"))

# Open the image (relative path)
image = Image.open("Defjam.png")

# Convert image to RGB mode once, so all manipulations are safe
image_rgb = image.convert("RGB")

# 1. Apply blur on RGB image
blurred = image_rgb.filter(ImageFilter.BLUR)
blurred.save("blurred_image.jpg")

# 2. Resize on RGB image
resized = image_rgb.resize((300, 300))
resized.save("resized_image.png")

# 3. Crop on RGB image (coordinates: left, upper, right, lower)
cropped = image_rgb.crop((100, 100, 400, 400))
cropped.save("cropped_image.png")

# 4. Grayscale conversion
gray = image_rgb.convert("L")  # 'L' is grayscale mode
gray.save("grayscale_image.png")

# 5. Rotate image by 45 degrees
rotated = image_rgb.rotate(45)
rotated.save("rotated_image.png")

print("All image operations completed successfully!")

image.show()
