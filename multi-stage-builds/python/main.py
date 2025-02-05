import cv2
import numpy as np
import os


def main():
    # Create output directory path
    output_dir = "/app/output"

    # Create a sample image
    img = np.zeros((300, 300, 3), np.uint8)
    cv2.circle(img, (150, 150), 100, (0, 255, 0), -1)

    # Write to the output directory
    output_path = os.path.join(output_dir, "circle.png")
    cv2.imwrite(output_path, img)
    print(f"Created {output_path}")


if __name__ == "__main__":
    main()
