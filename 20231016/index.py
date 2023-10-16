import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("1000x800+300+50")
        self.title("lines")
        self.configure(background="#F8C3CD")

class MyFrame(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master,**kwargs)
        self.configure(background="#C73E3A")
        self.img = Image.open("pets.png")
        self.pets = ImageTk.PhotoImage(self.img)
        canvas = tk.Canvas(self,
                           width=1000,
                           height=800)
        
        canvas.create_image(500,400,image=self.pets,anchor=tk.CENTER)
        canvas.pack()
        self.pack(expand=1 ,fill='both')

        ''' canvas = tk.Canvas(self)
        canvas.create_line(15,30,200,30)
        canvas.create_line(300,10,300,300,500,450,300,10, dash=(1,1))
        canvas.pack(expand=1,fill="both")
        self.pack(expand=1,fill="both") '''


def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__=='__main__':
    main()