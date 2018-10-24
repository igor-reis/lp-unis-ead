#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
3)	Faça um programa que leia 3 números inteiros e mostre o menor deles.
"""

a = input('Digite o número A: ')
b = input('Digite o número B: ')
c = input('Digite o número C: ')

if (a < b) & (a < c):
    print 'O menor número é:', a
elif (b < a) & (b < c):
    print 'O menor número é:', b
elif (c < a) & (c < b):
    print 'O menor número é:', c
