from PIL import Image

def file_to_image(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    img = Image.new("1", (100, 100), color="white")
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            pixel = int(lines[y * 100 + x].strip())
            img.putpixel((x, y), pixel)

    return img

img2 = file_to_image("stormborn.txt")
img2.save("out.png")