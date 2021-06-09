from PIL import Image
import os
os.chdir(os.path.dirname(__file__))
SCALE = 60

def get_color(str):
    im = Image.open(str)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    region = int(width/SCALE)
    result = []
    for i in range(0,SCALE):
        r,g,b = 0,0,0
        for j in range(0,region):
            r += pix[i * region + j, height-1][0]
            g += pix[i * region + j, height-1][1]
            b += pix[i * region + j, height-1][2]
        r = int(r / region)
        g = int(g / region)
        b = int(b / region)
        result.append([r,g,b])
    return result

if __name__ == "__main__":
    a = get_color("./pic.jpg")
    print(a)
    print(a[0])