import datetime

#並び替え関数
def list_sort(lis_join, file):
    words_base = []
    words = []
    new_words_list = []         
    new_words = ""
    dic = {}
    num = 0

    

    with open(file, "r") as f:
        words_base = f.readlines()
    if lis_join != "" or lis_join != []:
        if type(lis_join) == str:
           words_base.append(lis_join)
        elif type(lis_join) == list:
            for i in range(len(lis_join)):
                words_base.append(lis_join)

    #リストに整える
    for i in words_base:
        if i.endswith("\n"):
            i_1 = i.strip()
            a = i_1.split("|")
        else:
            a = i.split("|")
        words.append([a])

        #シリアル値を計算
        num = datetime.datetime(int(a[1]), int(a[2]), int(a[3])) - datetime.datetime(1899, 12, 31)
        dic[num.days] = a

    #シリアル値をもとに並び替え
    dic_sorted = sorted(dic.items(), key=lambda x:x[0])

    #元に戻す
    for _, task_list in dic_sorted:
        new_word = "|".join(task_list)
        new_words_list.append(new_word)
        new_words = new_words + ("\n" if new_words != "" else "") + new_word
    with open(file, "w") as f:
        f.write(new_words)

    return new_words_list


#履歴作成関数
def make_log(current_file, log_file):

    live_tasks = []
    dead_tasks = []


    with open("task_log.txt") as f:
        dead = f.read()

    #現在のシリアル値を取得
    dt = str(datetime.datetime.now())
    dt = dt[:10]
    dt_list = dt.split("-")
    now_serial = datetime.datetime(int(dt_list[0]), int(dt_list[1]), int(dt_list[2])) - datetime.datetime(1899, 12, 31)

    with open(current_file, "r") as f:
        tasks_base = f.readlines()

    #リストに整える
    for i in tasks_base:
        if i.endswith("\n"):
            i_1 = i.strip()
            a = i_1.split("|")
        else:
            a = i.split("|")

        #シリアル値で分類
        num = datetime.datetime(int(a[1]), int(a[2]), int(a[3])) - datetime.datetime(1899, 12, 31)
        serial = num.days
        if int(serial) < int(now_serial.days):
            dead_tasks.append(i)
        else:
            live_tasks.append(i)
            with open(current_file, "w") as f:
                f.writelines(live_tasks)

    list_sort(dead_tasks, log_file)
