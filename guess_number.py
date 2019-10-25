#! usr/bin/python3
# -*- coding:utf-8 -*-

import random
secret = random.randint(1, 10)
print("-----数字游戏-----")
temp = input("猜测一个数字(只有三次机会):")
total_degree = 1
residue_degree = 3
while True:
    try:
        guess = int(temp)
        if guess == secret:
            print("猜对了")
        else:
            if guess > secret:
                print("大了")
            else:
                print("小了")
        while guess != secret and total_degree < 3:
            total_degree = total_degree + 1
            residue_degree -= 1
            temp = input("猜错了，请重新输入(还剩余" + str(residue_degree) + "次机会):")
            guess = int(temp)
            if guess == secret:
                print("猜对了")
            else:
                if guess > secret:
                    print("大了")
                else:
                    print("小了")
        print("游戏结束,正确答案是:" + str(secret))
        break
    except ValueError:
        temp = input("输入的不是数字，请重新输入数字(还剩余" + str(residue_degree) + "次机会):")

