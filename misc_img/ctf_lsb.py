"""
LSB隐写，得到ctf_lsb.png是一个二维码
"""
from PIL import Image

img = Image.open("img.png")
width, height = img.size
for i in range(0, width):
    for j in range(0, height):
        tmp = img.getpixel((i, j))
        if tmp & 0x1 == 0:
            img.putpixel((i, j), 0)
        else:
            img.putpixel((i, j), 255)
img.show()
img.save("ctf_lsb.png")
