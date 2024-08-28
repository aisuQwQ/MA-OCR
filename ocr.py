from paddleocr import PaddleOCR
from PIL import Image

import logging
logging.disable(logging.DEBUG)

print('Preparing...')
ocr = PaddleOCR(use_angle_cls=True, use_gpu=False, lang="ch")
print("Ready!")

import pyautogui
import numpy
from PIL import ImageEnhance

def readScreen():
    im=pyautogui.screenshot()
    #コントラスト増加
    enhancer=ImageEnhance.Contrast(im)
    im=enhancer.enhance(2)
    #型変換
    im=numpy.array(im)
    result=ocr.ocr(im, cls=True)[0]
    
    #result[n th][place or txt][place num]
    # left,top=result[0][0][0]
    # right,bottom=result[0][0][2]
    

    texts = [line[1][0] for line in result]

    print("❦================================================❦")
    for t in texts:
        print(t)
    return result