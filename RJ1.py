#課題1-1
import tkinter as tk
root = tk.Tk()
root.geometry("400x300")
canvas = tk.Canvas(root, bg = "white")
canvas.create_rectangle(100, 100, 300, 200,fill='black')
canvas.pack()
root.mainloop()

#課題1-2
import tkinter as tk
root = tk.Tk()
canvas = tk.Canvas(root, height=600, width=1000)
canvas.create_rectangle(450, 150, 550, 200,fill='black')
canvas.create_rectangle(400,200,600,270,fill='black')
canvas.create_oval(410,270,450,310,fill='black')
canvas.create_oval(550,270,590,310,fill='black')
canvas.create_text(500,350,text = "Yui Moroyama")
canvas.pack()
root.mainloop()