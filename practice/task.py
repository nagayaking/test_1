my_task = input("あなたのタスクを入力")

with open("task.txt","a") as f:
    f.write(my_task)