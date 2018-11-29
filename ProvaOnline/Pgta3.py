#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parouimpar(v):
    if v%2==0:
        print("O número", v, "é par")
    else:
        print("O número", v, "é ímpar")

n = int(input('Digite um número: '))
parouimpar(n)