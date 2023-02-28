from PIL import Image

def hide_text_in_image(text, image_path, output_image_path):
    image = Image.open(image_path)
    binary_text = ''.join(format(ord(i), '08b') for i in text)
    index = 0
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            if index < len(binary_text):
                r = (r & ~1) | int(binary_text[index])
                index += 1
            if index < len(binary_text):
                g = (g & ~1) | int(binary_text[index])
                index += 1
            if index < len(binary_text):
                b = (b & ~1) | int(binary_text[index])
                index += 1
            image.putpixel((x, y), (r, g, b))
    image.save(output_image_path)

hide_text_in_image(open('flag.txt').read(), "ironman.png", "output.png")