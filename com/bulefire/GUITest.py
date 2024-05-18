import tkinter as tk
import requests

global a
a = 1
data = {"did": " ", "player": 1, "color": "RED", "number": 2}


def http(data):
    headers = {'Content-Type': 'application/json'}
    re = requests.post("http://localhost:8080/api/CtrlCards", json=data, headers=headers)
    return re.text


def button(color, number):
    global a

    result = http(data)
    b = a
    if a < 4:
        a = a + 1
    elif a == 4:
        a = 1
    else:
        label = tk.Label(root, text="??????")
        label.pack()  # 将标签放置在窗口中

    label = tk.Label(root, text=(result + " " + str(a)))
    label.pack()


root = tk.Tk()

# 标题
root.title("test")
# 大小
root.geometry("300x800")

button1 = tk.Button(root, text="按钮文字", command=lambda: button("RED", 8))  # command参数指定按钮被点击时调用的函数
button1.pack()
# 在窗口上创建一个标签控件


root.mainloop()
