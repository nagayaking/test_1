import tkinter as tk
from tkinter import ttk
import datetime 
import calendar

selected_value_year = 1
selected_value_month = 1
selected_value_date = 1
dates = []

#ひと月の長さ
def month_range(year,month):
    day, range = calendar.monthrange(year, month)
    return range
with open("task.txt", "r") as f:
    taskss = f.read()

#並び替え
def list_sort(lis_join, lis_base, file):
    dic = {}
    lis_key = ["task", "year", "month", "date"]
    words_base = []
    with open(file, "r") as f:
        words_base = f.readlines()
    words_join = lis_join.split("|")
    

#現在の年月日を取得
dt = datetime.datetime.now
current = dt()
year = current.year
month = current.month
date = current.date

#曜日と年のリスト
days = {0:"月曜日", 1:"火曜日", 2:"水曜日", 3:"木曜日", 4:"金曜日", 5:"土曜日", 6:"日曜日"}
years = []
for i in range(year,year + 11):
    years.append(i)

#初期設定
root = tk.Tk()
root.title(u"my_task")
root.geometry("400x300")

#ラベル
Static1 = tk.Label(text=u"タスクを入力")
Static2 = tk.Label(text=u"年を入力")
Static3 = tk.Label(text=u"月を入力")
Static4 = tk.Label(text=u"日付を入力")
Static5 = tk.Label(text=u"現在のタスク")
list_tasks =tk.Label(text=taskss,background="#f0f8ff")

Static1.grid(row=0, column=0, columnspan=2, sticky = tk.N+tk.S)
Static2.grid(row=1, column=0, columnspan=2, sticky = tk.N+tk.S)
Static3.grid(row=2, column=0, columnspan=2, sticky = tk.N+tk.S)
Static4.grid(row=3, column=0, columnspan=2, sticky = tk.N+tk.S)
Static5.grid(row=6,column=0)
list_tasks.grid(row=7, column=0, columnspan=5, sticky=tk.W, padx=10)

#エントリー
Editbox =tk.Entry()
Editbox.grid(row=0, column=3)

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
    rng = 0
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
        combobox_3.grid(row=3,column=3)

    combobox_2.bind("<<ComboboxSelected>>", on_select)
    combobox_2.grid(row=2,column=3)

combobox_1.bind("<<ComboboxSelected>>", on_select)
combobox_1.grid(row=1,column=3)


#送信ボタンと更新
def button_clicked():
    global tasks, taskss
    value = get_value()
    with open("task.txt", "r") as f:
        tasks = f.readlines()
    if tasks == []:
        with open("task.txt", "w") as f:
            f.write(f"{value}|{selected_value_year}|{selected_value_month}|{selected_value_date}")
        taskss = taskss + f"{value}|{selected_value_year}|{selected_value_month}|{selected_value_date}"
        list_tasks =tk.Label(text=taskss,background="#f0f8ff")
        list_tasks.grid(row=7, column=0, columnspan=5, sticky=tk.W, padx=10)
    else:
        with open("task.txt", "a") as f:
            f.write(f"\n{value}|{selected_value_year}|{selected_value_month}|{selected_value_date}")
        taskss = taskss + f"\n{value}|{selected_value_year}|{selected_value_month}|{selected_value_date}"
        list_tasks =tk.Label(text=taskss,background="#f0f8ff")
        list_tasks.grid(row=7, column=0, columnspan=5, sticky=tk.W, padx=10)

button = tk.Button(root, text="送信", command=button_clicked)
button.grid(row=4, column=0, pady=10)


root.mainloop()