import tkinter as tk 
root = tk.Tk()
root.geometry('600x500')
canvas = tk.Canvas(root, height=500, width=600)
def draw_car(x,y,scale,color):
    canvas.create_rectangle(x, y, x+50*scale, y+25*scale,fill=color,outline=color)
    canvas.create_rectangle(x-25*scale,y+25*scale,x+75*scale,y+60*scale,fill=color,outline=color)
    canvas.create_oval(x-20*scale,y+60*scale,x,y+80*scale,fill='black')
    canvas.create_oval(x+50*scale,y+60*scale,x+70*scale,y+80*scale,fill='black')
draw_car(225,75,1,'red')
draw_car(450,150,2,'blue')
canvas.pack()
root.mainloop()

