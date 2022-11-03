import cv2 as cv
from PIL import ImageGrab
  
isDragging = False
x1,y1,x2,y2 = -1,-1,-1,-1
blue,red = (255,0,0),(0,0,255)
 
def onMouse(event, x,y,flags, param):
    global isDragging,x1,y1,img
    if event ==cv.EVENT_LBUTTONDOWN:
        isDragging=True
        x1=x
        y1=y
    elif event==cv.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw=img.copy()
            cv.rectangle(img_draw,(x1,y1),(x,y),blue,2)
            cv.imshow('img',img_draw)
    elif event== cv.EVENT_LBUTTONUP:
        if isDragging:
            isDragging=False
            x2=x
            y2=y
            print('x:%d, y%d,w:%d,h:%d'%(x1,y1,x2,y2))
 
            img_draw= img.copy()
            cv.rectangle(img_draw,(x1,y1),(x2,y2),red,2)
            cv.imshow('img',img_draw)
            if x1>x2:
                x1,x2=x2,x1
            if y1>y2:
                y1,y2=y2,y1
 
            roi = img[y1:y2,x1:x2]
            cv.imshow('capture',roi)
            # cv.moveWindow('cropped',0,0)
            cv.imwrite('./save.jpg',roi)
            print('capture')
 
img=ImageGrab.grab()
img.save('./screenshot.jpg')
 
img=cv.imread('./screenshot.jpg',cv.IMREAD_COLOR)
 
cv.imshow('img',img)
cv.setMouseCallback('img',onMouse)
cv.waitKey()
cv.destroyAllWindows()