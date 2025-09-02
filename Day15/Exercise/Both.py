import pandas as pd
from PIL import Image
import os

data = [
    {"Date": "2025-01-10", "Region": "North", "Salesperson": "John Doe", "Product": "Laptop", "Units Sold": 5, "Unit Price": 900, "Total Revenue": 4500},
    {"Date": "2025-01-12", "Region": "South", "Salesperson": "Jane Smith", "Product": "Tablet", "Units Sold": 10, "Unit Price": 300, "Total Revenue": 3000},
    {"Date": "2025-01-13", "Region": "East", "Salesperson": "Bob Johnson", "Product": "Smartphone", "Units Sold": 7, "Unit Price": 500, "Total Revenue": 3500},
    {"Date": "2025-01-15", "Region": "West", "Salesperson": "Alice Lee", "Product": "Laptop", "Units Sold": 3, "Unit Price": 900, "Total Revenue": 2700},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Print basic info and stats
print("=== Dataset Info ===")
print(df.info())
print("\n=== Summary Statistics ===")
print(df.describe(include='all'))

# Group total revenue by salesperson
print("\n=== Total Revenue by Salesperson ===")
print(df.groupby('Salesperson')['Total Revenue'].sum())

print("#"*45)


# Path to your image file (replace with your actual image path)
image_path = "/home/faisalabufarah/Desktop/python-backend/Day15/Hands-on/Defjam.png"

if os.path.exists(image_path):
    # Open image
    img = Image.open(image_path)
    
    # Convert to grayscale
    gray_img = img.convert("RGB")
    
    # Save grayscale image
    gray_img.save("grayscale_output.png")
    
    print(f"\nImage '{image_path}' processed and saved as 'grayscale_output.png'.")
else:
    print(f"\nImage file '{image_path}' not found. Please provide a valid image path.")
gray_img.show()