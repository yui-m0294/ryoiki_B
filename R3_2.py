import tkinter as tk

root = tk.Tk()
root.geometry('700x700')
canvas = tk.Canvas(root, height=700, width=700)

canvas.create_rectangle(225, 75, 275, 100,fill='red',outline='red',tag="id1")
canvas.create_rectangle(200,100,300,135,fill='red',outline='red',tag="id1")
canvas.create_oval(205,135,225,155,fill='black',tag="id1")
canvas.create_oval(275,135,295,155,fill='black',tag="id1")
canvas.pack()

def key_event(e):
   key = e.keysym
   x, y = 0, 0
   if key == "Up":
       y -= 10
   if key == "Down":
       y += 10
   if key == "Left":
       x -= 10
   if key == "Right":
       x += 10      
   canvas.move("id1", x, y)
root.bind("<KeyPress>", key_event)
root.mainloop()
