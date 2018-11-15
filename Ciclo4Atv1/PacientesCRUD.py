from Banco import Banco


class Pacientes(object):

    def __init__(self, cpf="", nome="", endereco="", altura="", peso="", imc=""):
        self.info = {}
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.altura = altura
        self.peso = peso
        self.imc = imc

    def insertPaciente(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute('''INSERT INTO pacientes(cpf, nome, endereco, altura, peso, imc)
                VALUES(?,?,?,?,?,?)''', (self.cpf, self.nome, self.endereco, self.altura, self.peso, self.imc))

            banco.conexao.commit()
            c.close()

            return "Paciente registrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do paciente"

    def updatePaciente(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute('''UPDATE pacientes SET nome = ?, endereco = ?, altura = ?, peso = ?, imc = ?
                WHERE cpf = ?''',(self.nome, self.endereco, self.altura, self.peso, self.imc, self.cpf))

            banco.conexao.commit()
            c.close()

            return "Paciente atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do paciente"

    def deletePaciente(self):

        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("DELETE FROM pacientes WHERE cpf = " + self.cpf + " ")

            banco.conexao.commit()
            c.close()

            return "Paciente excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do paciente"

    def selectPaciente(self, cpf):
        banco = Banco()
        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM pacientes WHERE cpf = " + cpf + "  ")

            for linha in c:
                self.cpf = linha[0]
                self.nome = linha[1]
                self.endereco = linha[2]
                self.altura = linha[3]
                self.peso = linha[4]
                self.imc = linha[5]

            c.close()

            return self.cpf
        except:
            return "Ocorreu um erro na busca do paciente"