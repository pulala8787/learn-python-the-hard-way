# bulls and cows

import random
import sys

def dead():
    print("I am sorry, but you have used out all your chances.")
    
print("天气这么热，不如跟我玩个小游戏呗")
print("现在，我脑子里有个20以内的数字")
print("你有10次机会可以猜我脑子里的数字是多少")
print("=========== BEGIN: ==========")

def input_num():
    temp = input("你猜的数字是: ")
    return temp

answer = random.randint(0,20)
chance=0
while chance < 10:
    chance = chance + 1 #循环不变式

    guess = input_num()
    if guess.isdigit() == False: #isdigit() 数字的函数
        print("我不懂你在说什么，请输入阿拉伯数字哦")
    elif int(guess) > answer:
        print("猜大了，")
    elif int(guess) < answer:
        print("猜小了")
    elif int(guess) == answer:
        print("Correct, awesome!")
        print("This round is over.")
        sys.exit()
    else:
        pass

dead()
