from PIL import Image
import os
os.chdir(os.path.dirname(__file__))
SCALE = 60

def get_color(str):
    im = Image.open(str)    #创建image对象
    pix = im.load()
    width = im.size[0]  #im是PIL库的对象，通过size列表获取图片尺寸
    height = im.size[1]
    region = int(width/SCALE)   #划分成SCALE个区域，region是每个区域的宽度
    result = []
    for i in range(0,SCALE):    #遍历SCALE个区，获取SCALE个RGB值
        r,g,b = 0,0,0
        for j in range(0,region):   #遍历region每个像素点
            r += pix[i * region + j, height-1][0]
            g += pix[i * region + j, height-1][1]
            b += pix[i * region + j, height-1][2]
        r = int(r / region)
        g = int(g / region)
        b = int(b / region) #r、g、b求平均值
        result.append([r,g,b])  #把求得的值添加到返回值中
    return result

if __name__ == "__main__":
    a = get_color("./pic.jpg")
    print(a)
    print(a[0])