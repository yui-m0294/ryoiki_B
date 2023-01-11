import tkinter as tk 
root = tk.Tk()
root.geometry('700x700')
root.configure(bg='white')
canvas = tk.Canvas(root, height=700, width=700)

def draw_car(x,y,scale,color):
    canvas.create_rectangle(x+15*scale,y+10*scale,x+20*scale,y+15*scale,fill=color,outline=color)
    canvas.create_rectangle(x+10*scale, y+15*scale, x+25*scale, y+20*scale,fill=color,outline=color)
    canvas.create_oval(x+11*scale,y+20*scale,x+15*scale,y+24*scale,fill='black')
    canvas.create_oval(x+20*scale,y+20*scale,x+24*scale,y+24*scale,fill='black')



for i in range(10):
    for j in range(10):
        if((i+j)%2==0):
            color ='blue'
        else:
            color = 'red'
        draw_car(50*j,50*i,3,color)
        #draw_car(250,95,1,color)
canvas.pack()

while True:
    x = input("キーボードから0～99の数値を入力してください")
    try:
        if(int(x)>=0 and int(x)<=99):
            draw_car(50*int(int(x)%10),50*int(int(x)/10),3,color="white")
            scale=3
            canvas.create_oval(50*int(int(x)%10)+11*scale,50*int(int(x)/10)+20*scale,50*int(int(x)%10)+15*scale,50*int(int(x)/10)+24*scale,fill='white',outline="white")
            canvas.create_oval(50*int(int(x)%10)+20*scale,50*int(int(x)/10)+20*scale,50*int(int(x)%10)+24*scale,50*int(int(x)/10)+24*scale,fill='white',outline="white")
            root.update()  
        else:
            print("入力が0～99以外の数値になっています")

    except:
        print("入力が文字列になっています")
        break


