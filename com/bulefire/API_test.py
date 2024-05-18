import requests

# data = {"did": " ", "player": 1, "color": "RED", "number": 2}
data = {"pl": "4"}


def http_post(date, url):
    headers = {'Content-Type': 'application/json'}
    re = requests.post("http://localhost:8080" + url, json=date, headers=headers)
    print(re.text +"\n")


def http_get(url):
    headers = {'Content-Type': 'application/json'}
    re = requests.get("http://localhost:8080" + url, headers=headers)
    print(re.text + "\n")


while True:
    number = int(input("1:房主发起请求 2:成员发起请求 3:游戏是否开始 4:发牌 5:退出" + "\n"))
    if number == 1:
        pl = int(input("玩家数" + "\n"))
        model = input("model" + "\n")
        url = "/api/post/masterStartGet"
        date = {"pl": pl, "model": model}
        http_post(date, url)
    elif number == 2:
        url = "/api/get/memberStartGet"
        http_get(url)
    elif number == 3:
        url = "/api/get/isStart"
        http_get(url)
    elif number == 4:
        player = int(input("PLAYER:" + "\n"))
        color = input("COLOR:")
        number = int(input("NUMBER:" + "\n"))
        url = "/api/post/CtrlCards"
        date = {"did": " ", "player": player, "color": color, "number": number}
        http_post(date, url)
    elif number == 5:
        break
