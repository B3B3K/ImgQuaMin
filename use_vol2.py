import cv2
import numpy as np

# Load the image
image_path = "test_r.jpg"
image = cv2.imread(image_path)
h, w, _ = image.shape

# Print the height and width
print(f"Height (h): {h} pixels")
print(f"Width (w): {w} pixels")

# Define the size of each split area
split_size = 2

width = w 
height = h 
blank_image = np.zeros((height, width, 3), np.uint8)

# Get the dimensions of the image
height, width, _ = image.shape

# Create an empty list to store the average color and coordinates of each split area
split_areas = []

# Iterate over the image in split_size intervals
for y in range(0, height, split_size):
    for x in range(0, width, split_size):
        # Calculate the coordinates of the split area
        x1 = x
        y1 = y
        x2 = x + split_size
        y2 = y + split_size

        # Extract the split area from the image
        split_area = image[y1:y2, x1:x2]

        # Calculate the average color of the split area
        average_color = np.mean(split_area, axis=(0, 1))

        # Store the average color and coordinates in the list
        split_areas.append((x1, y1, x2, y2, average_color))

for i, (x1, y1, x2, y2, color) in enumerate(split_areas):
    color_int = color.astype(int)
    try:
        for x in range(x1, x2):
            for y in range(y1, y2):
                blank_image[y, x, :] = color_int
    except:
        pass
    #for owerflowing, if it happens, change height and weight (?) or add +1 to h and w

# Save the modified image
output_image_path = "modified_image.jpg"
cv2.imwrite(output_image_path, blank_image)
print(f"Modified image saved as {output_image_path}")
