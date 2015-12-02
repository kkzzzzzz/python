__author__ = 'Kevin'
from PIL import Image
import glob, os

size = 128, 128


width = 0
height = 0

# file_new  = []
# i = 0
# for infile in glob.glob("../../Desktop/pic/*.jpg"):
#     file, ext = os.path.splitext(infile)
#     print file
#     print ext
#     file_new.append(infile)
#     im = Image.open(infile)
#     if im.size[0] > width:
#         width = im.size[0]
#     height = im.size[1]
#     im.thumbnail(size, Image.ANTIALIAS)
#     # im.save(file + "thumbnail"+".jpg", "JPEG")

image_open = Image.open(r"../../Desktop/pic/3.png")

image_to_merge = Image.open(r"../../Desktop/pic/1.jpg")
resize = image_to_merge.resize((image_open.size[0], image_open.size[1]))


for x in range(0, image_open.size[0]):
    for y in range(0, image_open.size[1]):
        getpixel = resize.getpixel((x, y))
        new_rgb = (getpixel[0], getpixel[1], getpixel[2], 255)
        image_open.putpixel((x,y), new_rgb)


# image_open.show()
# open1.show()
# paste = image_open.paste(image_open, open1)
# paste.show()
# image_open_bg = Image.open(r"../../Desktop/pic/3.png")
# bg_resize = image_open_bg.resize((2 * image_open.size[0], image_open.size[1]))
# bg_resize.show()

merge_img = Image.new('RGBA', (2*image_open.size[0],image_open.size[1]), (255,255,255,255))
open2 = Image.open(r"../../Desktop/pic/3.png")

for x in range(0, open2.size[0]):
    for y in range(0, open2.size[1]):
        getpixel = open2.getpixel((x, y))
        new_rgb = (getpixel[0], getpixel[1], getpixel[2], 20)
        open2.putpixel((x,y), new_rgb)
merge_img.paste(image_open,(0,0),image_open)
merge_img.paste(open2,(0,0),open2)
merge_img.show()




