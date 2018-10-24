#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
4)	Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.
"""

def numPrimo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

num_inicial = 1
num_final = 100

for i in range(num_inicial, num_final+1):
    resultado = numPrimo(i)
    if resultado:
        print i,'Verdadeiro'
    else: print i, 'Falso'