import tkinter as tk  # 視窗
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import tkinter.font as tkFont
import datasource as ds
import tkintermapview  # 地圖
import os
import base64


# 標籤
class TKLable(tk.Label):
    def __init__(self, parents, **kwargs):
        super().__init__(parents, **kwargs)
        helv26 = tkFont.Font(family="微軟正黑體", size=12, weight="bold")  # 先設定字體格式
        self.config(font=helv26)  # ,foreground="#FFFFFF"


# 一般按鈕
class TKButton(tk.Button):
    def __init__(self, parents, **kwargs):  # **kwargs 打包
        super().__init__(parents, **kwargs)  # **kwargs 打開


# Treeview
class CustomFrame(tk.Frame):
    def __init__(self, parent, data=None, map_widget=None, **kwargs):  # 這裡的self是定義
        super().__init__(parent, **kwargs)

        self.list_data = data
        self.tree = ttk.Treeview(
            self, columns=["#1", "#2", "#3", "#4"], show="headings", height=10
        )
        self.tree.pack(side=tk.LEFT, padx=10)

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)

        self.tree.heading("#1", text="地址")
        self.tree.heading("#2", text="車號")
        self.tree.heading("#3", text="抵達時間")
        self.tree.heading("#4", text="離開時間")

        self.tree.column("#1", width=300, anchor=tk.W)
        self.tree.column("#2", width=100, anchor="center")
        self.tree.column("#3", width=70, anchor="center")
        self.tree.column("#4", width=70, anchor="center")

        for item in self.list_data:
            self.tree.insert("", tk.END, values=item)

        # treeview綁定
        def print_element(event):
            tree = event.widget
            curItem = tree.focus()
            address = tree.item(curItem)["values"][0]  # 地址
            x = float(tree.item(curItem)["values"][4])  # 經度
            y = float(tree.item(curItem)["values"][5])  # 緯度

            # selection = [tree.item(item)["values"] for item in tree.selection()]
            # print(type(selection))
            # print("selected items:", selection)
            # 把地圖的定位定在點選的那列資料
            map_widget.set_position(x, y)
            map_widget.set_zoom(18)
            messagebox.showinfo("已完成", f"已將{address}定位到地圖！", parent=tree)

        self.tree.bind("<Double-1>", print_element)


# 主視窗設定
class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="#345678")  # 設定背景藍色

        # 建立Label pack是由上而下!
        title = tk.Label(self, text="Fish", bg="#345678")  # 類似CSS padding的設定 上下左右各推30
        titlefont = tkFont.Font(family="微軟正黑體", size=18, weight="bold")  # 先設定字體格式
        title.config(font=titlefont, foreground="#FFFFFF")
        title.pack(padx=10, pady=10)

        # 新增 KeywordFrame
        self.KeywordFrame = ttk.Frame(self, width=800, height=500)
        self.KeywordFrame.pack(fill="both", expand=True)

        # ------區域時段搜尋框架--------
        # 放選單的框架
        mainFrame = tk.Frame(self.KeywordFrame, width=800, height=500)
        mainFrame.pack()

        # 建立關鍵字的label
        TKLable(mainFrame, text="以下可擇一搜尋，搜尋到的結果雙擊兩下可以到地圖區看到位置", bd=3).grid(
            row=0, column=0, columnspan=4
        )

        # 建立Combo的Label
        TKLable(mainFrame, text="綱", bd=3).grid(row=1, column=0)
        # 抓取台北行政區
        self.TaipeiArea_dict = ds.Get_TaipeiArea()
        # 台北市行政區下拉選單
        self.TaipeiAreaValue = tk.StringVar()
        self.TaipeiArea_Combo = ttk.Combobox(
            mainFrame,
            values=list(self.TaipeiArea_dict.keys()),
            justify="center",
            textvariable=self.TaipeiAreaValue,
        )
        self.TaipeiArea_Combo.grid(row=1, column=1)
        self.TaipeiArea_Combo.current(0)

        # 綁定選擇區域事件
        self.TaipeiArea_Combo.bind(
            "<<ComboboxSelected>>", self.change_AreaVillage_Combo
        )

        TKLable(mainFrame, text="目").grid(row=1, column=2)
        # 村里下拉選單(依據選擇的行政區連動)
        self.AreaVillageValue = tk.StringVar()
        self.AreaVillage_Combo = ttk.Combobox(
            mainFrame,
            values=["全部"],
            justify="center",
            textvariable=self.AreaVillageValue,
        )
        self.AreaVillage_Combo.grid(row=1, column=3)
        self.AreaVillage_Combo.current(0)

        # 建立關鍵字的label
        TKLable(mainFrame, text="街道名稱", bd=3).grid(row=2, column=0)
        self.Search = tk.Entry(mainFrame, width=55)
        self.Search.grid(row=2, column=1, columnspan=3)

        # 建立抵達時間的Label
        TKLable(mainFrame, text="抵達時間(起)").grid(row=3, column=0)
        self.TimeStart = tk.Entry(mainFrame, width=22)
        self.TimeStart.grid(row=3, column=1)
        TKLable(mainFrame, text="抵達時間(迄)").grid(row=3, column=2)
        self.TimeEnd = tk.Entry(mainFrame, width=23)
        self.TimeEnd.grid(row=3, column=3)

        # 搜尋按鈕
        self.keyButton = TKButton(mainFrame, text="搜尋", command=self.KeySearch)
        self.keyButton.config(width=60)
        self.keyButton.grid(row=4, columnspan=4)

    # 下拉連動選單
    def change_AreaVillage_Combo(self, event):
        towncode01 = self.TaipeiArea_dict[self.TaipeiAreaValue.get()]
        value = ds.Get_AreaVillage(towncode01)
        self.AreaVillage_Combo.config(values=value)
        self.AreaVillage_Combo.current(0)

    # 區域地區關鍵字搜尋
    def KeySearch(self):
        Road = ""  # 街道名稱
        Towncode01 = ""  # 行政區
        Towncode02 = ""  # 村里
        TimeStart = ""  # 抵達時間起
        TimeEnd = ""  # 抵達時間迄

        if self.Search.get() != "":
            Road = self.Search.get()
        if self.TaipeiAreaValue.get() != "全區":
            Towncode01 = self.TaipeiAreaValue.get()
        if self.AreaVillageValue.get() != "全部":
            Towncode02 = self.AreaVillageValue.get()
        if self.TimeStart.get() != "":
            TimeStart = self.TimeStart.get().replace(":", "")
        if self.TimeEnd.get() != "":
            TimeEnd = self.TimeEnd.get().replace(":", "")

        # 抵達時間不可以只輸入一個
        if self.TimeStart.get() != "" and self.TimeEnd.get() == "":
            messagebox.showwarning("請輸入欄位", "抵達時間(迄)請勿空白", parent=self.keyButton)
            return
        elif self.TimeStart.get() == "" and self.TimeEnd.get() != "":
            messagebox.showwarning("請輸入欄位", "抵達時間(起)請勿空白", parent=self.keyButton)
            return

        # print("視窗的值:",Road,Towncode01,Towncode02,TimeStart,TimeEnd)
        keydata = []
        for item in self.garbagestation_list:
            Roadcheck = False
            Towncode01check = False
            Towncode02check = False

            x = float(item["經度"])  # 25.05081974
            y = float(item["緯度"])  # 121.5438535
            address = item["地點"]  # 臺北市中山區復興北路66號
            TaipeiArea = item["行政區"]  # 中山區
            AreaVillage = item["里別"]  # 力行里
            carNum = item["車號"]  # 119-BQ
            timeS = item["抵達時間"]  # 1700
            timeE = item["離開時間"]  # 1709

            # 都沒輸入，印全部
            if (
                Road == ""
                and Towncode01 == ""
                and Towncode02 == ""
                and TimeStart == ""
                and TimeEnd == ""
            ):
                timeS = f'{item["抵達時間"][:2]}:{item["抵達時間"][2:]}'  # 1700
                timeE = f'{item["離開時間"][:2]}:{item["離開時間"][2:]}'  # 1709
                keydata.append([address, carNum, timeS, timeE, x, y])
            else:  # 根據搜尋條件來印對應資料
                Towncode01check = TaipeiArea.__contains__(Towncode01)
                Towncode02check = AreaVillage.__contains__(Towncode02)
                Roadcheck = address.__contains__(Road)

                if Towncode01check and Towncode02check and Roadcheck:
                    # 時間區間
                    if TimeStart != "":
                        if int(float(timeS)) >= int(float(TimeStart)) and int(
                            float(timeS)
                        ) <= int(float(TimeEnd)):
                            timeS = f'{item["抵達時間"][:2]}:{item["抵達時間"][2:]}'  # 1700
                            timeE = f'{item["離開時間"][:2]}:{item["離開時間"][2:]}'  # 1709
                            keydata.append([address, carNum, timeS, timeE, x, y])
                    else:
                        timeS = f'{item["抵達時間"][:2]}:{item["抵達時間"][2:]}'  # 1700
                        timeE = f'{item["離開時間"][:2]}:{item["離開時間"][2:]}'  # 1709
                        keydata.append([address, carNum, timeS, timeE, x, y])

        # LabelFrame
        if hasattr(self, "displayFrame"):
            self.displayFrame.destroy()
        self.displayFrame = ttk.LabelFrame(
            self.KeywordFrame,
            text=f"\n查詢結果({len(keydata)}筆)",
            borderwidth=2,
            relief=tk.GROOVE,
        )
        self.displayFrame.pack(fill=tk.BOTH, padx=80, pady=(0, 30))
        if len(keydata) != 0:
            # print(keydata)
            dataFrame = CustomFrame(
                self.displayFrame, data=keydata, map_widget=self.map_widget
            )
            dataFrame.pack(side=tk.LEFT)
        else:
            TKLable(self.displayFrame, text="oops...沒有垃圾車資訊唷").pack(padx=10, pady=10)


# 主程式
def main():
    window = Window()
    window.title("Fish")
    window.resizable(0, 0)  # 禁止拖拉視窗調整視窗大小
    window.geometry("800x500")
    window.mainloop()


if __name__ == "__main__":
    main()
