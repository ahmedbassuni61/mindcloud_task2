from PIL import Image, ImageFilter
img = Image.open("mind.jpg")
img.show()
width, height = img.size
pixels = img.load()
for x in range(width//4):
    for y in range(height):
        pixels[x, y] = (0, 0, 0) 
img.save("left_quarter_black.jpg")
img.show()