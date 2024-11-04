from PIL import Image

image = Image.open('monro.jpg')
image = image.convert('RGB')
red, green, blue = image.split()

pixel_offset = 50

red_left = red.crop((pixel_offset, 0, red.width, red.height))
blue_right = blue.crop((0, 0, (blue.width - pixel_offset), blue.height))

red_middle = red.crop((pixel_offset/2, 0, (red.width - pixel_offset/2), red.height))
blue_middle = blue.crop((pixel_offset/2, 0, (blue.width - pixel_offset/2), blue.height))
green_middle = green.crop((pixel_offset/2, 0, (green.width - pixel_offset/2), green.height))

new_red = Image.blend(red_left, red_middle, 0.5)
new_blue = Image.blend(blue_right, blue_middle, 0.5)

new_image = Image.merge('RGB', (new_red, green_middle, new_blue))
new_image.thumbnail((80, 80))
new_image.save('new_image.jpg')