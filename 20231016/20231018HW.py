import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import csv
import yfinance as yf
import pandas as pd
import os


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("台積電")


class MyFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack()

        #        scrollbar = ttk.Scrollbar(self, orient="vertical")
        #        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(
            self, columns=["#1", "#2", "#3", "#4", "#5", "#6", "#7"], show="headings"
        )
        self.tree.heading("#1", text="日期")
        self.tree.heading("#2", text="開盤價")
        self.tree.heading("#3", text="最高點")
        self.tree.heading("#4", text="最低點")
        self.tree.heading("#5", text="收盤價")
        self.tree.heading("#6", text="整後收盤價")
        self.tree.heading("#7", text="成交量")
        self.tree.pack()

        price = getdata()
        for row in price:
            self.tree.insert("", tk.END, value=row)

        self.tree.bind("<<TreeviewSelect>>")
        deletdata()

def getdata() -> list[list]:
    data = yf.download("2330.TW", start="2023-01-01")
    data.to_csv("台積電.csv")
    with open("台積電.csv", "r", encoding="UTF-8") as file:
        csvReader = csv.reader(file)
        next(csvReader)
        list_csvReader = [row for row in csvReader]
        return list_csvReader 

        


def deletdata():
    if os.path.exists("台積電.csv"):
        os.remove("台積電.csv")


def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()



if __name__ == "__main__":
    main()
