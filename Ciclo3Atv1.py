#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

class Application:
    def __init__(self, Application, master=None):
        self.fontePadrao = ("Arial", "10")

        self.Container1 = Frame(master)
        self.Container1["pady"] = 0
        self.Container1.pack()

        self.Container2 = Frame(master)
        self.Container2["padx"] = 0
        self.Container2.pack()

        self.Container3 = Frame(master)
        self.Container3["padx"] = 0
        self.Container3.pack()

        self.Container4 = Frame(master)
        self.Container4["pady"] = 0
        self.Container4.pack()

        self.Container5 = Frame(master)
        self.Container5["pady"] = 20
        self.Container5.pack()

        self.Container6 = Frame(master)
        self.Container6["pady"] = 5
        self.Container6.pack()

        self.Container7 = Frame(master)
        self.Container7["pady"] = 0
        self.Container7.pack()


        #Container Nome
        self.nomeLabel = Label(self.Container1, text="Nome do Paciente:", font=self.fontePadrao)
        self.nomeLabel["width"] = 15
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.Container1)
        self.nome["width"] = 50
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        self.nome.focus_set()


        # Container Endereço
        self.enderecoLabel = Label(self.Container2, text="Endereço Completo:", font=self.fontePadrao)
        self.enderecoLabel["width"] = 15
        self.enderecoLabel.pack(side=LEFT)

        self.endereco = Entry(self.Container2)
        self.endereco["width"] = 50
        self.endereco["font"] = self.fontePadrao
        self.endereco.pack(side=LEFT)


        # Container Altura
        self.alturaLabel = Label(self.Container3, text="Altura (cm):", font=self.fontePadrao)
        self.alturaLabel["width"] = 15
        self.alturaLabel.pack(side=LEFT)

        self.altura = Entry(self.Container3)
        self.altura["width"] = 5
        self.altura["font"] = self.fontePadrao
        self.altura.pack(side=LEFT)

        self.alturaLabelVazio = Label(self.Container3, text="", font=self.fontePadrao)
        self.alturaLabelVazio["width"] = 39
        self.alturaLabelVazio.pack(side=LEFT)


        # Container Peso
        self.pesoLabel = Label(self.Container4, text="Peso (Kg):", font=self.fontePadrao)
        self.pesoLabel["width"] = 15
        self.pesoLabel.pack(side=LEFT)

        self.peso = Entry(self.Container4)
        self.peso["width"] = 5
        self.peso["font"] = self.fontePadrao
        self.peso.pack(side=LEFT)

        self.pesoLabelVazio = Label(self.Container4, text="", font=self.fontePadrao)
        self.pesoLabelVazio["width"] = 39
        self.pesoLabelVazio.pack(side=LEFT)


        # Container Mensagem Nome e Endereço
        self.mensagemLabel = Label(self.Container5, text="", font=self.fontePadrao)
        self.mensagemLabel.pack()


        # Container Resultado
        self.mensagemResultadoLabel = Label(self.Container6, text="Resultado: ", font=self.fontePadrao, bg='light blue')
        self.mensagemResultadoLabel.pack(side=LEFT)
        self.resultadoLabel = Label(self.Container6, text="", font=self.fontePadrao)
        self.resultadoLabel.pack(side=LEFT)

        self.mensagemImcResultadoLabel = Label(self.Container6, text="IMC: ", font=self.fontePadrao, bg='light blue')
        self.mensagemImcResultadoLabel.pack(side=LEFT)
        self.imcResultadoLabel = Label(self.Container6, text="", font=self.fontePadrao)
        self.imcResultadoLabel.pack(side=LEFT)


        # Container Botões
        self.calcular = Button(self.Container7)
        self.calcular["text"] = "Calcular"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.CalcularIMC
        self.calcular.pack(side=LEFT)

        self.reiniciar = Button(self.Container7)
        self.reiniciar["text"] = "Reiniciar"
        self.reiniciar["font"] = ("Calibri", "8")
        self.reiniciar["width"] = 12
        self.reiniciar["command"] = self.Limpar
        self.reiniciar.pack(side=LEFT)

        self.sair = Button(self.Container7)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 12
        self.sair["command"] = Application.quit
        self.sair.pack(side=LEFT)


    # Método calcular IMC
    def CalcularIMC(self):
        nome = self.nome.get()
        endereco = self.endereco.get()

        self.mensagemLabel["text"] = nome + '\n' + endereco

        alturaCM = float(self.altura.get())
        peso = float(self.peso.get())
        alturaM = alturaCM / 100

        IMC = peso / (alturaM * alturaM)

        if IMC < 16:
            self.resultadoLabel["text"] = "Magreza grave!"
            self.imcResultadoLabel["text"] = round(IMC, 2)
        elif (IMC >= 16) & (IMC < 17):
            self.resultadoLabel["text"] = "Magreza moderada!"
            self.imcResultadoLabel["text"] = round(IMC, 2)
        elif (IMC >= 17) & (IMC < 18.5):
            self.resultadoLabel["text"] = "Magreza leve!"
            self.imcResultadoLabel["text"] = round(IMC, 2)
        elif (IMC >= 18.5) & (IMC < 25):
            self.resultadoLabel["text"] = "Saudável!"
            self.imcResultadoLabel["text"] = round(IMC, 2)
        elif (IMC >= 25) & (IMC < 30):
            self.resultadoLabel["text"] = "Sobrepeso!"
            self.imcResultadoLabel["text"] = round(IMC, 2)
        elif (IMC >= 30) & (IMC < 35):
            self.resultadoLabel["text"] = "Obesidade Grau I!"
            self.imcResultadoLabel["text"] = round(IMC, 2)
        elif (IMC >= 35) & (IMC < 40):
            self.resultadoLabel["text"] = "Obesidade Grau II (severa)!"
            self.imcResultadoLabel["text"] = round(IMC, 2)
        elif IMC > 40:
            self.resultadoLabel["text"] = "Obesidade Grau III (mórbida)!"
            self.imcResultadoLabel["text"] = round(IMC, 2)


    # Método limpar
    def Limpar(self):
        self.nome.delete(0, END)
        self.endereco.delete(0, END)
        self.altura.delete(0, END)
        self.peso.delete(0, END)
        self.mensagemLabel["text"] = ""
        self.resultadoLabel["text"] = ""
        self.imcResultadoLabel["text"] = ""
        self.nome.focus_set()


root = Tk()
root.title('Cálculo do IMC - Índice de Massa Corporal')
Application(root)
root.mainloop()