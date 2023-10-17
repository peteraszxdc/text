import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import csv


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title("2330台積電")


class Frame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack()

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.tree = ttk.Treeview(
            self,
            columns=[1, 2, 3, 4, 5, 6, 7],
            show="headings",
            yscrollcommand=scrollbar.set,
        )
        scrollbar.configure(command=self.tree.yview)
        self.tree.heading(1, text="日期")
        self.tree.heading(2, text="開盤價")
        self.tree.heading(3, text="盤中最高價")
        self.tree.heading(4, text="盤中最低價")
        self.tree.heading(5, text="收盤價")
        self.tree.heading(6, text="調整後收盤價")
        self.tree.heading(7, text="成交量")
        self.tree.pack()

        price = getPrice()
        for row in price:
            self.tree.insert("", tk.END, values=row)

        self.tree.bind("<<TreeviewSelect>>")


def getPrice() -> list[list]:
    with open("台積電.csv", "r", encoding="UTF-8") as file:
        csvReader = csv.reader(file)
        next(csvReader)
        list_csvReader = list(csvReader)
    return list_csvReader


def main():
    window = Window()
    frame = Frame(window)
    window.mainloop()


if __name__ == "__main__":
    main()
