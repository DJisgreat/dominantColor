import cv2
import numpy as np 
from datetime import datetime
from matplotlib import pyplot as plt 

hlist=[20,40,75,155,190,270,290,316,360]
svlist=[21,178,255]

def quantilize(h,s,v):
    '''hsv直方图'''
    #value:[21,144,23]h,s,v
    h=h*2
    for i in range(len(hlist)):
        if h<=hlist[i]:
            h=i%8
            break
    for i in range(len(svlist)):
        if s<=svlist[i]:
            s=i
            break
    for i in range(len(svlist)):
        if v<=svlist[i]:
            v=i
            break
    return 9*h+3*s+v

quantilize_ufunc=np.frompyfunc(quantilize,3,1)
# 自定义ufunc函数，即将quantilize函数转化为ufunc函数，其输入参数为３个，输出参数为１个。


def colors(img):
    hsv=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    nhsv=quantilize_ufunc(hsv[:,:,0],hsv[:,:,1],hsv[:,:,2]).astype(np.uint8)
    # 由于frompyfunc函数返回结果为对象，所以需要转换类型
    hist=cv2.calcHist([nhsv],[0],None,[72],[0,71])
    hist=hist.reshape(1,hist.shape[0]).astype(np.int32).tolist()[0]
    return hist

if __name__=='__main__':
    img=cv2.imread('cloth1.jpg')
    colors(img)


    