#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

#fórmula de Heron para calculo da área

a = input('Digite o lado A: ')
b = input('Digite o lado B: ')
c = input('Digite o lado C: ')

#calcular semiperímetro
p = (a + b + c) / 2

#calcular area
area = p * (p-a)*(p-b)*(p-c)

if area > 0:
   raiz = math.sqrt(area)
   print "É um triângulo com área igual a", round(raiz, 2)
else:
   print "Não é um triangulo! \nA =", a, "\nB =", b, "\nC =", c

