# Turtle Hirst Dot Painting

This project uses Python's `turtle` graphics module to create a Hirst-style dot painting. The program generates a grid of randomly colored dots, each 20 pixels in diameter, based on a predefined color palette. The canvas is designed to be 10x10 dots, with each dot spaced 50 pixels apart.

## Features

- Creates a 10x10 grid of dots using the `turtle` module.
- Uses random colors from a predefined list of RGB values.
- Dot size: 20 pixels.
- Spacing between dots: 50 pixels.

## Getting Started

### Prerequisites

- Python 3.x
- `turtle` module (built-in to Python)

### Optional Step (Color Extraction)

The color list used in this project can be generated from any image using the colorgram library, although the script currently includes a predefined color list. If you'd like to extract colors from an image:

Install colorgram.py:

### Uncomment the code block that generates the color list from an image in the script

import colorgram

rgb_colors = []
colors = colorgram.extract("image.jpg", 10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
