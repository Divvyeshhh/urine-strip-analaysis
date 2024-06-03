import cv2
import numpy as np
from PIL import Image

def process_image(image):
    img = Image.open(image)
    img = np.array(img)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    height = 100
    aspect_ratio = height / img_rgb.shape[0]
    img_rgb = cv2.resize(img_rgb, (int(img_rgb.shape[1] * aspect_ratio), height))

    segment_width = img_rgb.shape[1] // 10
    colors = []
    for i in range(10):
        segment = img_rgb[:, i*segment_width:(i+1)*segment_width]
        avg_color = segment.mean(axis=(0, 1)).astype(int)
        colors.append(avg_color.tolist())

    return colors
