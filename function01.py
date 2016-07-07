# -*- coding: utf-8 -*-

import sys

start_number = int(input("Enter the start number: "))
end_number = int(input("Enter the end number: "))


def sum_me(start, end):
    sum = 0
    if start_number > end_number:
        print("Are you kidding, man?")
        print("The start number should less equal than the end number")
        sys.exit()

    while start <= end:
        sum += start_number
        start += 1

    print("The sum is: %d" % sum)

sum_me(start_number, end_number)

