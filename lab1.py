#!/usr/bin/env python3
# coding=utf-8

def lab1():

    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x > 5:
        y = (5 * a * b) / (pow(x, 2) + pow(a, 2))
    else:
        y = 4 * (pow((a + b - x), 2))

    print("y = %.1f" % y)
    input("Нажмите Enter для выхода")

if __name__ == '__main__':
    lab1()
