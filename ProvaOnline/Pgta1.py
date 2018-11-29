#!/usr/bin/env python
# -*- coding: utf-8 -*-

def proximofibonacci(x, y, c):
    for i in range(3, c+1):
        s = x+y
        print(s)
        x = y
        y = s

a = 0
b = 1
c = 10

print(a)
print(b)

proximofibonacci(a, b, c)

