import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.simpledialog import Dialog
import yfinance as yf
import csv

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)        
        self.title("台積電")

def getdata()-> list[list]:
    date = yf.download("2330.TW",start='2023-01-01')
    with open(date) as file:
        csvReader = csv.reader(file)
        next(csvReader)
        list_csvReader = list(csvReader)
    return list_csvReader

class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)

        self.tree = ttk.Treeview(self,columns=['#1', '#2', '#3', '#4', '#5', '#6', '#7'],show="headings")
        self.tree.heading('#1', text="日期")
        self.tree.heading('#2', text="開盤價")
        self.tree.heading('#3', text="最高點")
        self.tree.heading('#4', text="最低點")
        self.tree.heading('#5', text="收盤價")
        self.tree.heading('#6', text="整後收盤價")
        self.tree.heading('#7', text="成交量")

        price = getdata()
        for row in price:
            self.tree.insert('',tk.END,value=row)

        
        self.tree.pack()

        self.tree.bind('<<TreeviewSelect>>',self.item_selected)

       
        
    def item_selected(self,event):
        item_id = self.tree.selection()[0]
        item_dict = self.tree.item(item_id)
        #print(item_dict['values'])

        
    


def main():    
    window = Window()
    myFrame = MyFrame(window,"對齊方式")    
    window.mainloop()

if __name__ == "__main__":
    main()