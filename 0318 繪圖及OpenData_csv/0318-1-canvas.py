import tkinter as tk
from PIL import ImageTk, Image

win = tk.Tk()

c1 = tk.Canvas(win, width=1100, height=800)     #建立Canvas畫布 繪圖





c1.create_line(450,100,650,100, fill="red", width=5)     #畫線 width粗度
c1.create_line(550,50,450,250, fill="blue", width=5)
c1.create_line(550,50,650,250, fill="green", width=5)
c1.create_line(450,250,650,100, fill="pink", width=5)
c1.create_line(450,100,650,250, fill="yellow", width=5)

c1.create_text(550,450,text="ya!ya!ya!ya!",font=('Forte',100))                   #寫文字



def paint( event ):                                     #畫畫功能
   python_green = "#476042"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   c1.create_oval( x1, y1, x2, y2, fill = python_green )        #畫圓點
#  c1.create_rectangle(x1,y1,x2,y2,fill="blue")                 #畫其他圖形
#  c1.create_image(x1,y1,image=img)

c1.bind( "<B1-Motion>", paint )


c1.pack()
win.mainloop()