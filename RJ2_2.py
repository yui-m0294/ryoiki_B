import tkinter as tk 
root = tk.Tk()
root.geometry('600x600')
canvas = tk.Canvas(root, height=600, width=600)
def draw_car(x,y,scale,color):
    canvas.create_rectangle(x+15*scale,y+10*scale,x+20*scale,y+15*scale,fill=color,outline=color)
    canvas.create_rectangle(x+10*scale, y+15*scale, x+25*scale, y+20*scale,fill=color,outline=color)
    canvas.create_oval(x+11*scale,y+20*scale,x+15*scale,y+24*scale,fill='black')
    canvas.create_oval(x+20*scale,y+20*scale,x+24*scale,y+24*scale,fill='black')
    
for i in range(10):
    for j in range(10):
        if(i+j)%2==0:
            color ='blue'
        else:
            color = 'red'
        draw_car(50*j,50*i,3,color)
canvas.pack()
root.mainloop()
