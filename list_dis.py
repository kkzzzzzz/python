__author__ = 'Kevin'
import numpy

list = [1,2,3]
narray=numpy.array(list)
sum1=narray.sum()
print(sum1)
narray2=narray*narray
sum2=narray2.sum()
print(sum2)
mean=sum1/3
var=sum2/3-mean**2
print(var)


list = [1,2,3]
mean = numpy.mean(list)
a = ((list[0]-mean)**2+(list[1]-mean)**2+(list[2]-mean)**2)/3
print(a)

narray=numpy.array(list)
sum1=narray.sum()
narray2=narray*narray
sum2=narray2.sum()
mean=sum1/3
var=sum2/3-mean**2