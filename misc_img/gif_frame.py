"""
把gif图片的frame分别保存
gif帧数能开平方，可能拼成二维码

PIL的mode
modes	描述
1	    1位像素，黑和白，存成8位的像素
L	    8位像素，黑白
P	    8位像素，使用调色板映射到任何其他模式
RGB	    3× 8位像素，真彩
RGBA	4×8位像素，真彩+透明通道
CMYK	4×8位像素，颜色隔离
YCbCr	3×8位像素，彩色视频格式
I	    32位整型像素
F	    32位浮点型像素

"""
from PIL import Image
import os

fname = 'gif_frame.gif'
name = fname[:-4]
os.mkdir(name)  # 创建同名目录

img = Image.open(fname)
print(f'gif size: {img.size}, gif mode: {img.mode}')
try:
    while True:
        cur = img.tell()  # 当前frame
        img.save(f'{name}\\{name}_{cur}.png') # 原样保存每个frame

        # img_gray = img.convert('L')  # 转黑白，根据实际情况调整
        # img_gray.save(f'{name}\\{name}_{cur}.png')
        # print(img_gray.getpixel((img_gray.size[0] // 2, img_gray.size[1] // 2)),
        #       end=',') # 打印出每个frame的像素值

        img.seek(cur + 1)  # 下一个frame
except EOFError:
    pass
