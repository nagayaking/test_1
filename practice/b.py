import datetime


def list_sort(lis_join, file):
    dic = {}
    lis_key = ["task", "year", "month", "date"]
    words_base = []
    words = []
    num = 0

    with open(file, "r") as f:
        words_base = f.readlines()
    words_base.append(lis_join)
    for i in words_base:
        if i.endswith("\n"):
            i_1 = i.strip()
        a = i_1.split("|")
        for j in range(4):
            key = lis_key[j] + str(num)
            dic[key] = a[j]
        j = 0
        words.append([a])
        num += 1
    
    print(dic)

dt = datetime.datetime(2001,3,26) - datetime.datetime(1899, 12, 31)
print(dt.days) # シリアル値

list_sort("finnfj|y|m|d", "task.txt")