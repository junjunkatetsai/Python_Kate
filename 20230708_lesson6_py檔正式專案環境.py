#!/usr/bin/python3.10.4

import random

min = 1
max = 10
count = 0
target = random.randint(min,max)
print('----猜數字遊戲-----\n')

while True:
    keyin = int(input(f'猜數字範圍{min}~{max}:'))
    count += 1
    if (keyin == target):
        print(f'賓果! 猜對了,答案是:{target}')
        print(f'您共猜了{count}次')
        break
    else:
        print(f'猜錯了')
        print(f'您共猜了{count}次')
print('遊戲結束')