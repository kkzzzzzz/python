__author__ = 'Kevin'

# coding: UTF-8
import re
link = re.compile("\<.*?\>")

content = '<td> sdfsdf </td>'
info = re.sub(link,' ',content)
print info

