#!/usr/bin/python
# w1.py

import sys

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
    if inputInfo == "history" :
        print(historyCities)
    elif inputInfo == "help" :
        print("输入Help，获取帮助文档")
        print("输入history，获取查询历史")
        print("输入quit，退出天气查询系统")
        print("输入你想要查询的城市名")
    elif inputInfo == "quit" :
        sys.exit()
    else :
        historyCities.append(inputInfo)
        printCityWeather(inputInfo)
