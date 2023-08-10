from PIL import Image
import numpy as np
import time


# 打开图像文件
image1 = Image.open("cxk_right.png")
image1 = image1.convert("RGB")  # 将图像转换为RGB模式
# 获取图像的宽度和高度
width1, height1 = image1.size

# 打开图像文件
image2 = Image.open("cxk_left.png")
image2 = image2.convert("RGB")  # 将图像转换为RGB模式
# 获取图像的宽度和高度
width2, height2 = image2.size

# 颜色映射函数
def map_color(color):
    r, g, b = color
    # 根据 RGB 值计算最接近的 ANSI 颜色代码
    code = 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)
    return code
    
output1 = ""
for y in range(height1):
    for x in range(width1):
        pixel_color = image1.getpixel((x, y))
        ansi_code = f"\033[48;5;{map_color(pixel_color)}m  \033[0m"
        output1 += ansi_code
    output1 += "\n"

output2 = ""
for y2 in range(height2):
    for x2 in range(width2):
        pixel_color = image2.getpixel((x2, y2))
        ansi_code = f"\033[48;5;{map_color(pixel_color)}m  \033[0m"
        output2 += ansi_code
    output2 += "\n"

while True:
    print(output1)
    time.sleep(1)
    print(output2)
    time.sleep(1)