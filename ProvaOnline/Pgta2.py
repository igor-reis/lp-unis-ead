#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

#Janela principal
win = Tk()
win.title("Aplicação para a Prova Online - Python")
win.resizable(0,0)

#Converte maisculo
def upperCase():
    text = entry.get("1.0",END)
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, text.upper())
    output.config(state=DISABLED)

#Converte minusculo
def lowerCase():
    text = entry.get("1.0",END)
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.insert(END, text.lower())
    output.config(state=DISABLED)

#Limpar
def clean():
    entry.delete('1.0', END)
    output.config(state=NORMAL)
    output.delete('1.0', END)
    output.config(state=DISABLED)

#Cria Widgets
l1 = Label(win, text="CAIXA ALTA e caixa baixa")
entry = Text(win, width=70, height=3, wrap=WORD)
button1 = Button(win, text="Tudo MAISCÚLO", width=15)
button2 = Button(win, text="Tudo MINÚSCULO", width=15)
button3 = Button(win, text="LIMPAR", width=15)
output = Text(win, width=70, height=3, wrap=WORD)
output.config(state=DISABLED)

#Posiciona os Widgets
l1.grid(row=1, column=1, padx=5, sticky=W)
entry.grid(row=2, column=1, columnspan=2, padx=5, pady=(0,10))
button1.grid(row=3, column=1, columnspan=1, pady=5)
button2.grid(row=3, column=2, columnspan=1, pady=5)
button3.grid(row=4, column=2, columnspan=1, pady=5)
output.grid(row=5, column=1, columnspan=2, padx=5, pady=(0,10))

#Botão "Tudo MAISCÚLO"
button1.configure(command=upperCase)

#Botão "Tudo MINÚSCULO"
button2.configure(command=lowerCase)

#Botão "LIMPAR"
button3.configure(command=clean)

win.mainloop()