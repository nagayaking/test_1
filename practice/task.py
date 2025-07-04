import tkinter as tk
from tkinter import ttk
import datetime 
import calendar

import library

selected_value_year = 1
selected_value_month = 1
selected_value_date = 1
dates = []

#ひと月の長さ
def month_range(year,month):
    _, range = calendar.monthrange(year, month)
    return range
with open("task.txt", "r") as f:
    taskss = f.readlines()


#現在の年月日を取得
dt = datetime.datetime.now
current = dt()
year = current.year
month = current.month
date = current.date

#曜日と年のリスト
years = []
for i in range(year,year + 11):
    years.append(i)

#初期設定
root = tk.Tk()
root.title(u"my_task")
root.geometry("400x300")
library.make_log("task.txt", "task_log.txt")
with open("task_log.txt") as f:
    log = f.readlines()


#ラベル
Static1 = tk.Label(text=u"タスクを入力")
Static2 = tk.Label(text=u"年を入力")
Static3 = tk.Label(text=u"月を入力")
Static4 = tk.Label(text=u"日付を入力")
Static5 = tk.Label(text=u"現在のタスク")
Static6 = tk.Label(text=u"タスクの履歴")

#リストの選択
list_tasks = tk.StringVar(value=tuple(taskss))
list_log = tk.StringVar(value=tuple(log))

#各種ウィジェットの作成
Listbox1 = tk.Listbox(root, listvariable=list_tasks, height=5)
Listbox2 = tk.Listbox(root, listvariable=list_log,height=5)

#スクロールバーの作成
scrollbar1 = tk.Scrollbar(root, orient=tk.VERTICAL, command=Listbox1.yview)
scrollbar2 = tk.Scrollbar(root, orient=tk.VERTICAL, command=Listbox2.yview)

 # スクロールバーをListboxに反映
Listbox1["yscrollcommand"] = scrollbar1.set
Listbox2["yscrollcommand"] = scrollbar2.set

#グリッドの設置
Static1.grid(row=0, column=0, columnspan=2, sticky = tk.N+tk.S)
Static2.grid(row=1, column=0, columnspan=2, sticky = tk.N+tk.S)
Static3.grid(row=2, column=0, columnspan=2, sticky = tk.N+tk.S)
Static4.grid(row=3, column=0, columnspan=2, sticky = tk.N+tk.S)
Static5.grid(row=6,column=0)
Static6.grid(row=6,column=2)
Listbox1.grid(row=7, column=0)
scrollbar1.grid(row=7, column=1, sticky=(tk.N, tk.S))
Listbox2.grid(row=7, column=2)
scrollbar2.grid(row=7, column=3, sticky=(tk.N, tk.S))

#エントリー
Editbox = tk.Entry()
Editbox.grid(row=0, column=2)

value = 0
def get_value():
    global value
    return Editbox.get()

#コンボボックス

#年を取得
combobox_1 = ttk.Combobox(root, values = years)
def on_select(event):
    global selected_value_year
    selected_value_year = int(combobox_1.get())
    print("選択された値:", selected_value_year)

    #月を取得
    months = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    combobox_2 = ttk.Combobox(root, values = months)
    def on_select(event):
        global selected_value_month, dates
        selected_value_month = int(combobox_2.get())
        rng = month_range(selected_value_year, selected_value_month)
        for i in range(1, rng):
            dates.append(i)
        print("選択された値:", selected_value_month)

        #日を取得
        combobox_3 = ttk.Combobox(root, values = dates)
        def on_select(event):
            global selected_value_date
            selected_value_date = combobox_3.get()
            print("選択された値:", selected_value_date)
            print(f"選択した日付は{selected_value_year}年{selected_value_month}月{selected_value_date}日です")
        combobox_3.bind("<<ComboboxSelected>>", on_select)
        combobox_3.grid(row=3,column=2)

    combobox_2.bind("<<ComboboxSelected>>", on_select)
    combobox_2.grid(row=2,column=2)

combobox_1.bind("<<ComboboxSelected>>", on_select)
combobox_1.grid(row=1,column=2)


#送信ボタンと更新
def button_clicked():
    global tasks
    selected_value_task = get_value()
    with open("task.txt", "r") as f:
        tasks = f.readlines()
    join_task = f"{selected_value_task}|{selected_value_year}|{selected_value_month}|{selected_value_date}"
    new_tasks = library.list_sort("hhh|2027|5|29", "task.txt")
    list_tasks = tk.StringVar(value=tuple(new_tasks))
    Listbox1 = tk.Listbox(root, listvariable=list_tasks, height=5)
    scrollbar1 = tk.Scrollbar(root, orient=tk.VERTICAL, command=Listbox1.yview)
    Listbox1["yscrollcommand"] = scrollbar1.set
    Listbox1.grid(row=7, column=0)
    scrollbar1.grid(row=7, column=1, sticky=(tk.N, tk.S))
    print(11111111111)


button = tk.Button(root, text="送信", command=button_clicked)
button.grid(row=3, column=5)


root.mainloop()