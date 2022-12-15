import colorgram

rgb_colors = []
# Extract 6 colors from an image.
colors = colorgram.extract('spot.jpg', 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)