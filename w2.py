#!/usr/bin/python
# w2.py

import sys
import requests
import json

def printOnlineWeather(inputCity):
    r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city=" + inputCity)
    if r.status_code == 200:
        resp = r.text # 定义resp 保存 对象 r 的属性 r.text
        weatherjson = json.loads(resp)  # get 请求
        status = weatherjson["status"]
        if status != 1000:
            print("请输入汉字城市名才可以获知天气哦")
        if status == 1000:
            TodayWeather = weatherjson["data"]["forecast"][0]
            print("今天是" + TodayWeather["date"] + "," + inputCity
            + "气温是" + TodayWeather["high"] + TodayWeather["low"] + ","
            + "天气是" + TodayWeather["type"]+ ","
            #+ "风力是" + TodayWeather["fengli"]+","
            + "风向是" + TodayWeather["fengxiang"])
    else:
        print("网络忘记了")



def printCityWeather(inputCity) :
    txt = open("w1_weather_info.txt")
    for line in txt:
        temp = line.split(",")
        # 找城市，出天气
        city = temp[0]
        weather = temp[1]
        if city == inputCity :
            print("城市" + city + "的天气是" + weather)
            txt.close()
            return
    ## end for
    print("没有找到" + inputCity + "的天气")
    txt.close()


##Start
historyCities = []
while True:
    inputInfo = input("请输入城市或者指令：")
    if inputInfo == "history" or inputInfo == "his":
        print(historyCities)
    elif inputInfo == "help" :
        print("输入Help，获取帮助文档")
        print("输入history or his，获取查询历史")
        print("输入quit，退出天气查询系统")
        print("输入你想要查询的城市名")
    elif inputInfo == "quit" :
        sys.exit()
    else :
        historyCities.append(inputInfo)
        printOnlineWeather(inputInfo)
