from turtle import Turtle, Screen
import random

# create turtle objects
t = Turtle()
s = Screen()

# Set color mode to 255 to accept RGB values
s.colormode(255)

# set turtle speed
t.speed("fastest")

# Step 1: Generate a list of RGB colors from an image
"""import colorgram

rgb_colors = []
# extracting colors from an image
colors = colorgram.extract("image.jpg", 10)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)  # tuple
    rgb_colors.append(new_color)

print(rgb_colors)
"""
# Step 2: Define the color list from rgb_colors
color_list = [
    (230, 222, 218),
    (231, 224, 228),
    (223, 221, 228),
    (218, 173, 125),
    (159, 181, 190),
    (134, 73, 53),
    (50, 103, 154),
    (118, 81, 92),
    (179, 142, 152),
    (162, 104, 151),
]

# Use Turtle to draw Hirst painting
# Need to be 10 by 10 dimensions
# Need to be 20 dots in size spaced 50 pixels apart


def top_left_corner():
    t.penup()
    t.goto(-250, 250)  # this is the top left corner of the canvas
    t.pendown()


def draw_dots(x, y, row, dots_per_row):
    # repeat z times
    for _ in range(row):  # of rows
        for _ in range(dots_per_row):  # of dots per row
            t.penup()
            t.goto(x, y)
            t.dot(20, random.choice(color_list))  # this is the dot size and color
            x += 50  # move to the right by 50 pixels for the next dot
        y -= 50  # move down by 50 pixels for the next row
        x = -250  # reset x to the leftmost position for the next row


top_left_corner()
draw_dots(-250, 250, 10, 10)
s.exitonclick()
