#!/usr/bin/env python
# -*- coding: latin1 -*-

"""
1)	Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.
"""

idade = input('Digite sua idade em dias: ')
a = idade/365
m = idade/30
d = idade
print "Sua idade em anos:", a, "- meses:", m, "- dias:", d

