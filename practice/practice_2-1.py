year = 2900

if year%4 != 0:
    print("平年です")
else:
    if year%100 == 0:
        if year%400 != 0:
            print("平年です")
        else:
            print("閏年です")
    else:
        print("閏年です")