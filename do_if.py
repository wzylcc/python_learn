# -*- coding: utf-8 -*-

height = 1.75
weight = 80.5

bmi = int(weight / height ** 2)

if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
