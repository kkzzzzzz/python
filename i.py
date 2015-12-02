import random

__author__ = 'Kevin'
from PIL import Image
import glob, os
import numpy


def clipResizeImg(ori_img, dst_w, dst_h):

    im = ori_img
    ori_w,ori_h = im.size

    dst_scale = float(dst_h) / dst_w

    width = ori_w
    height = int(width*dst_scale)

    x = 0
    y = (ori_h - height) / 3

    if(height>ori_h):
        height = ori_h
        width = ori_h/ dst_scale

        y = 0
        x = (ori_w - width)/2


    print(width,height)
    box = (x,y,width+x,height+y)
    newIm = im.crop(box)
    return newIm.resize((dst_w,dst_h),Image.ANTIALIAS)

def getSameValue(background,file_new_png):
    target_id = 0
    target_total_dis = 0
    i = 0
    for img in file_new_png:
        total_dis = 0
        for x in range(0, img.size[0]):
            for y in range(0, img.size[1]):
                getpixel = img.getpixel((x, y))
                background_getpixel = background.getpixel((x, y))
                list = [getpixel[0]-background_getpixel[0],getpixel[1]-background_getpixel[1],getpixel[2]-background_getpixel[2]]
                narray=numpy.array(list)
                sum1=narray.sum()
                narray2=narray*narray
                sum2=narray2.sum()
                mean=sum1/3.0
                var=sum2/3.0-mean**2
                total_dis = var+ total_dis
        print(total_dis)
        if(target_total_dis == 0):
            target_total_dis = total_dis
        i = i + 1
        if(target_total_dis>total_dis):
            target_id = i
            target_total_dis = total_dis
        print(target_total_dis)
    return file_new_png[target_id]


size = 72, 48


file_new  = []
i = 0
for infile in glob.glob("../../Desktop/travel/*.png"):
    image_open = Image.open(infile)
    file, ext = os.path.splitext(infile)
    im = Image.open(infile)
    img = clipResizeImg(im, size[0], size[1])
    file_new.append(img)
    i= i+1

print(i)


imq = Image.open(r"../../Desktop/test/3.png")
trans = imq.resize(size)
file_new_png = []

for img in file_new:
    merge_img = Image.new('RGBA', (size[0],size[1]), (255,255,255,255))
    for x in range(0, img.size[0]):
        for y in range(0, img.size[1]):
            getpixel = img.getpixel((x, y))
            new_rgb = (getpixel[0], getpixel[1], getpixel[2],125)
            merge_img.putpixel((x,y), new_rgb)
    file_new_png.append(merge_img)


bgtarget = Image.open(r"../../Desktop/test/1.jpg")
for x in range(0, bgtarget.size[0]):
    for y in range(0, bgtarget.size[1]):
        getpixel = bgtarget.getpixel((x, y))
        new_rgb = (getpixel[0], getpixel[1], getpixel[2], 225)
        bgtarget.putpixel((x,y), new_rgb)

# bgtarget = clipResizeImg(bgtarget,768,768)
files_new_len = len(file_new)

index_x = 0
index_y = 0
img_count = 0

while (index_y * size[1] < bgtarget.size[1]):
    while (index_x * size[0] < bgtarget.size[0]):
        img_count = img_count + 1
        bgtarget.paste(file_new_png[random.randint(0, files_new_len-1)], (index_x * size[0], index_y * size[1]),
                       file_new_png[random.randint(0, files_new_len-1)])
        # box = (index_x * size[0], index_y * size[1], (index_x + 1) * size[0], (index_y + 1) * size[1])
        # value = getSameValue(bgtarget.crop(box), file_new_png)
        # bgtarget.paste(value,(index_x * size[0], index_y * size[1]),value)
        index_x = index_x + 1
    index_x = 0
    index_y = index_y + 1
bgtarget.show()
