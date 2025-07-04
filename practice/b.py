import datetime

def list_sort(lis_join, file):
    words_base = []
    words = []
    new_words = ""
    dic = {}
    num = 0

    with open(file, "r") as f:
        words_base = f.readlines()
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
        new_words = new_words + ("\n" if new_words != "" else "") + new_word
    with open(file, "w") as f:
        f.write(new_words)