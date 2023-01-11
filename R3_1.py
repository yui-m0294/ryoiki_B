import tkinter as tk
import math
import time

root=tk.Tk()
root.geometry('700x400')

canvas=tk.Canvas(root,width=700,height=700,bg="white")
canvas.pack()

x = 20
y = 20
scale = 5
id1 = canvas.create_rectangle(x+15*scale,y+10*scale,x+20*scale,y+15*scale,fill="blue",outline="blue")
id2 = canvas.create_rectangle(x+10*scale, y+15*scale, x+25*scale, y+20*scale,fill="blue",outline="blue")
id3 = canvas.create_oval(x+11*scale,y+20*scale,x+15*scale,y+24*scale,fill='black')
id4 = canvas.create_oval(x+20*scale,y+20*scale,x+24*scale,y+24*scale,fill='black')

dx=5
dy=5
vx=2

while True:
    canvas.coords(id1,x+15*scale,y+10*scale,x+20*scale+dx,y+15*scale+dy) 
    canvas.coords(id2,x+10*scale,y+15*scale,x+25*scale+dx,y+20*scale+dy) 
    canvas.coords(id3,x+11*scale,y+20*scale,x+15*scale+dx,y+24*scale+dy) 
    canvas.coords(id4,x+20*scale,y+20*scale,x+24*scale+dx,y+24*scale+dy) 
    x+=vx 
    if x<=0: 
        vx=math.fabs(vx)
    elif x>=700: 
        vx=-math.fabs(vx) 
    time.sleep(0.01) 
    root.update()
root.mainloop()