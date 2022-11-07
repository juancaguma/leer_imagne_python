import easyocr
import cv2

IMG_P= 'imgs/cortinilla-solicita-credencial.png'

reader = easyocr.Reader(['en'])
RST = reader.readtext(IMG_P)
RST

for detection in RST:
    TEXT = detection[1]
    print(TEXT)
