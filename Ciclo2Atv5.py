#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
5)	Escreva uma função que:
a)	Receba uma frase como parâmetro.
b)	Retorne uma nova frase com cada palavra com as letras invertidas.
"""

def fraseInvertida(frase):
    return(frase[::-1])

frase = raw_input('Entre com uma frase: ')
print fraseInvertida(frase)
