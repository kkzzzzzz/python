__author__ = 'Kevin'
from PIL import Image
from os import path

__author__ = 'outofmemory.cn'

import os

size=48
newImg = Image.new('RGBA', (size*23, size))

for root,dirs,files in os.walk(r'C:\Users\outofmemory.cn\Desktop\48x48'):
    idx = 0
    for f in files:
        filePath = path.join(root,f)
        x = idx * size
        y = 0
        icon = Image.open(filePath)
        newImg.paste(icon, (x,y), mask=icon)
        idx += 1

newImg.save(r'e:\icons.png',"PNG")