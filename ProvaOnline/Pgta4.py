#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Digite três valores e descubra se eles formam um triângulo")
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os três valores formam um triângulo.")
else:
    print("Os três valores não formam um triângulo.")
