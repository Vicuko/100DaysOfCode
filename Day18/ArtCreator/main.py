import turtle as t
import colorgram

extracted_colors = colorgram.extract("DamienHirst.jpg", 6)
colors = list(map(lambda color: (color.rgb.r, color.rgb.g, color.rgb.b), extracted_colors))
print (colors)