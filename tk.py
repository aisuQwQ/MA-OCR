import tkinter as tk
# import mouse
import keyboard

import ctypes
#DPIスケーリングを無効にする
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import deepl

#
#初期じゅんび
#
root=tk.Tk()
root.title("MA OCR")
root.config(bg="#f0f0f0")
root.attributes("-transparentcolor", "#f0f0f0")
# root.attributes("-alpha", 0.5)
root.attributes('-fullscreen', True)
root.attributes("-topmost", True)

#キャンバス作成
class textCanvas(tk.Canvas):
    def __init__(self, root, ocr):
        super().__init__(root, width=70, height=70, bg="#f0f0f0")
        left,top=ocr[0][0]
        right,bottom=ocr[0][2]
        text=ocr[1][0]
        text=deepl.translate(text)
        canvas=tk.Canvas(root, width=right-left, height=bottom-top, bg="white")
        canvas.create_text((right-left)/2,(bottom-top)/2,text=text, width=(right-left))
        canvas.place(x=left, y=top)     
def notion(text):
    canvas=tk.Canvas(root, width=100, height=50, bg="white")
    canvas.create_text(50,25, text=text)
    canvas.place(x=0,y=0)


import threading
import ocr
from setting import OCR_KEY, DEL_KEY


def delcanvas(e):
    canvases=root.winfo_children()
    num=len(canvases)
    for canvas in canvases:
        canvas.destroy()
    if(num>1):
        notion('実行中')
keyboard.on_press_key(DEL_KEY, delcanvas)

def task(e):
    delcanvas(e)
    notion('OCR')
    results=ocr.readScreen()
    notion('翻訳')
    threads=[]
    for result in results:
        thread=threading.Thread(target=textCanvas, args=(root,result,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    notion('実行中')
    
    
keyboard.on_press_key(OCR_KEY, task)

notion('実行中')

def loop():
    root.after(1, loop)

root.after(1, loop)
root.mainloop()
print('end')
deepl.saveCache()
print('cache saved')