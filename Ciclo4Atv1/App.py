#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from PacientesCRUD import Pacientes

class Application:

    def __init__(self, Application, master=None):
        self.fontePadrao = ("Arial", "10")

        self.Container0 = Frame(master)
        self.Container0["pady"] = 0
        self.Container0.pack()

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

        self.Container8 = Frame(master)
        self.Container8["pady"] = 0
        self.Container8.pack()


        # Container CPF
        self.cpfLabel = Label(self.Container0, text="CPF do Paciente:", font=self.fontePadrao)
        self.cpfLabel["width"] = 15
        self.cpfLabel.pack(side=LEFT)

        self.cpf = Entry(self.Container0)
        self.cpf["width"] = 20
        self.cpf["font"] = self.fontePadrao
        self.cpf.pack(side=LEFT)
        self.cpf.focus_set()

        self.cpfLabelVazio = Label(self.Container0, text="", font=self.fontePadrao)
        self.cpfLabelVazio["width"] = 17
        self.cpfLabelVazio.pack(side=LEFT)

        # Método UPPERCASE
        def caps(event):
            nome.set(nome.get().upper())
            endereco.set(endereco.get().upper())

        #Container Nome
        self.nomeLabel = Label(self.Container1, text="Nome:", font=self.fontePadrao)
        self.nomeLabel["width"] = 15
        self.nomeLabel.pack(side=LEFT)

        nome = StringVar()
        self.nome = Entry(self.Container1, textvariable=nome)
        self.nome["width"] = 50
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        self.nome.bind("<KeyRelease>", caps)


        # Container Endereço
        self.enderecoLabel = Label(self.Container2, text="Endereço Completo:", font=self.fontePadrao)
        self.enderecoLabel["width"] = 15
        self.enderecoLabel.pack(side=LEFT)

        endereco = StringVar()
        self.endereco = Entry(self.Container2, textvariable=endereco)
        self.endereco["width"] = 50
        self.endereco["font"] = self.fontePadrao
        self.endereco.pack(side=LEFT)
        self.endereco.bind("<KeyRelease>", caps)


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
        self.calcular["width"] = 10
        self.calcular["command"] = self.calcularIMC
        self.calcular.pack(side=LEFT)

        self.cadastrar = Button(self.Container7)
        self.cadastrar["text"] = "Cadastrar"
        self.cadastrar["font"] = ("Calibri", "8")
        self.cadastrar["width"] = 10
        self.cadastrar["command"] = self.salvarPaciente
        self.cadastrar.pack(side=LEFT)
        self.cadastrar.configure(state=DISABLED)

        self.editar = Button(self.Container7)
        self.editar["text"] = "Editar"
        self.editar["font"] = ("Calibri", "8")
        self.editar["width"] = 10
        self.editar["command"] = self.alterarPaciente
        self.editar.pack(side=LEFT)
        self.editar.configure(state=DISABLED)

        self.excluir = Button(self.Container7)
        self.excluir["text"] = "Excluir"
        self.excluir["font"] = ("Calibri", "8")
        self.excluir["width"] = 10
        self.excluir["command"] = self.excluirPaciente
        self.excluir.pack(side=LEFT)
        self.excluir.configure(state=DISABLED)

        self.limpar = Button(self.Container7)
        self.limpar["text"] = "Limpar"
        self.limpar["font"] = ("Calibri", "8")
        self.limpar["width"] = 10
        self.limpar["command"] = self.limparTela
        self.limpar.pack(side=LEFT)

        self.sair = Button(self.Container7)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "8")
        self.sair["width"] = 10
        self.sair["command"] = Application.quit
        self.sair.pack(side=LEFT)

        self.buscar = Button(self.Container0)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 10
        self.buscar["command"] = self.buscarPaciente
        self.buscar.pack(side=LEFT)


        # Container Mensagem CRUD
        self.mensagemCRUDLabel = Label(self.Container8, text="", font=self.fontePadrao)
        self.mensagemCRUDLabel.pack()


    # Método calcular IMC
    def calcularIMC(self):

        if (self.nome.index("end") == 0) or (self.endereco.index("end") == 0) or (self.altura.index("end") == 0) or (self.peso.index("end") == 0):
            self.mensagemCRUDLabel["text"] = "Preencha todos os campos!"
        else:
            if self.mensagemCRUDLabel["text"] != "":
                self.mensagemCRUDLabel["text"] = ""
            paciente = Pacientes()
            cpf = self.cpf.get()
            alturaCM = float(self.altura.get())
            peso = float(self.peso.get())
            alturaM = alturaCM / 100

            IMC = peso / (alturaM * alturaM)

            self.validarIMC(IMC)

            if paciente.selectPaciente(cpf) == "":
                self.cadastrar.configure(state=NORMAL)
                self.cadastrar.focus_set()


    # Método validar IMC
    def validarIMC(self, imc):

        IMC = round(imc, 2)

        nome = self.nome.get()
        endereco = self.endereco.get()
        self.mensagemLabel["text"] = nome + '\n' + endereco

        if IMC < 16:
            self.resultadoLabel["text"] = "Magreza grave!"
            self.imcResultadoLabel["text"] = IMC
        elif (IMC >= 16) & (IMC < 17):
            self.resultadoLabel["text"] = "Magreza moderada!"
            self.imcResultadoLabel["text"] = IMC
        elif (IMC >= 17) & (IMC < 18.5):
            self.resultadoLabel["text"] = "Magreza leve!"
            self.imcResultadoLabel["text"] = IMC
        elif (IMC >= 18.5) & (IMC < 25):
            self.resultadoLabel["text"] = "Saudável!"
            self.imcResultadoLabel["text"] = IMC
        elif (IMC >= 25) & (IMC < 30):
            self.resultadoLabel["text"] = "Sobrepeso!"
            self.imcResultadoLabel["text"] = IMC
        elif (IMC >= 30) & (IMC < 35):
            self.resultadoLabel["text"] = "Obesidade Grau I!"
            self.imcResultadoLabel["text"] = IMC
        elif (IMC >= 35) & (IMC < 40):
            self.resultadoLabel["text"] = "Obesidade Grau II (severa)!"
            self.imcResultadoLabel["text"] = IMC
        elif IMC > 40:
            self.resultadoLabel["text"] = "Obesidade Grau III (mórbida)!"
            self.imcResultadoLabel["text"] = IMC


    # Método limpar
    def limparTela(self):

        self.cpf.delete(0, END)
        self.nome.delete(0, END)
        self.endereco.delete(0, END)
        self.altura.delete(0, END)
        self.peso.delete(0, END)
        self.mensagemLabel["text"] = ""
        self.resultadoLabel["text"] = ""
        self.imcResultadoLabel["text"] = ""
        self.mensagemCRUDLabel["text"] = ""
        self.cpf.focus_set()
        self.calcular.configure(state=NORMAL)
        self.editar.configure(state=DISABLED)
        self.excluir.configure(state=DISABLED)
        self.cadastrar.configure(state=DISABLED)


    # Método salvar
    def salvarPaciente(self):

        paciente = Pacientes()
        paciente.cpf = self.cpf.get()
        paciente.nome = self.nome.get()
        paciente.endereco = self.endereco.get()
        paciente.altura = self.altura.get()
        paciente.peso = self.peso.get()
        paciente.imc = self.imcResultadoLabel["text"]

        self.mensagemCRUDLabel["text"] = paciente.insertPaciente()
        self.cadastrar.configure(state=DISABLED)


    # Método buscar
    def buscarPaciente(self):

        paciente = Pacientes()
        cpf = self.cpf.get()
        paciente.selectPaciente(cpf)

        if paciente.cpf == "":
            self.mensagemCRUDLabel["text"] = "Paciente não encontrado!"
            self.calcular.configure(state=DISABLED)
        else:
            self.cpf.delete(0, END)
            self.cpf.insert(INSERT, paciente.cpf)
            self.nome.insert(INSERT, paciente.nome)
            self.endereco.insert(INSERT, paciente.endereco)
            self.altura.insert(INSERT, paciente.altura)
            self.peso.insert(INSERT, paciente.peso)

            self.editar.configure(state=NORMAL)
            self.excluir.configure(state=NORMAL)

            self.validarIMC(float(paciente.imc))

            self.mensagemCRUDLabel["text"] = "Busca feita com sucesso!"


    # Método editar
    def alterarPaciente(self):

        paciente = Pacientes()
        paciente.cpf = self.cpf.get()
        paciente.nome = self.nome.get()
        paciente.endereco = self.endereco.get()
        paciente.altura = self.altura.get()
        paciente.peso = self.peso.get()
        paciente.imc = self.imcResultadoLabel["text"]

        self.calcular.configure(state=DISABLED)
        self.limpar.focus_set()
        self.mensagemCRUDLabel["text"] = paciente.updatePaciente()


    # Método excluir
    def excluirPaciente(self):

        paciente = Pacientes()
        paciente.cpf = self.cpf.get()

        self.calcular.configure(state=DISABLED)
        self.limpar.focus_set()
        self.mensagemCRUDLabel["text"] = paciente.deletePaciente()


root = Tk()
root.title('Cálculo do IMC - Índice de Massa Corporal')
Application(root)
root.mainloop()