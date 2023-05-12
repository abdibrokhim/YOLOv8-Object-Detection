import numpy as np
import cv2
from typing import List, Tuple


def create_bar(height: int, width: int, color: List[int]) -> Tuple[np.ndarray, Tuple[int, int, int]]:
    """Create a bar of the given color."""
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar, (red, green, blue)


def get_dominant_color(image_path: str, number_clusters: int) -> List[Tuple[int, int, int]]:
    """Get the dominant color(s) in the given image."""
    img = cv2.imread(image_path)
    height, width, _ = np.shape(img)

    # Flatten the pixel values into a 2D array.
    pixel_values = np.reshape(img, (height * width, 3))
    pixel_values = np.float32(pixel_values)

    # Run k-means clustering on the pixel values.
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(pixel_values, number_clusters, None, criteria, 10, flags)

    # Create bars for each of the dominant colors.
    bars = []
    rgb_values = []
    for index, row in enumerate(centers):
        bar, rgb = create_bar(200, 200, row)
        bars.append(bar)
        rgb_values.append(rgb)

    return rgb_values


if __name__ == "__main__":
    img = "data/train/macbook.jpg"
    number_clusters = 1
    print(get_dominant_color(img, number_clusters))
