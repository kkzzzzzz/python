__author__ = 'Kevin'
from PIL import Image
from PIL import ImageFilter

imp = Image.open(r"../../Desktop/pic/2.png")

size = imp.size[0], imp.size[1]

imq = Image.open(r"../../Desktop/pic/2.png")
trans = imq

trans.show()
trans_filter = trans.filter(ImageFilter.BLUR)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.CONTOUR)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.DETAIL)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.EDGE_ENHANCE)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.EDGE_ENHANCE_MORE)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.EMBOSS)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.FIND_EDGES)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.SMOOTH)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.SMOOTH_MORE)
trans_filter.show()
trans_filter = trans.filter(ImageFilter.SHARPEN)
trans_filter.show()
