import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists pacientes (
                     cpf text primary key,
                     nome text,
                     endereco text,
                     altura text,
                     peso text,
                     imc text)""")
        self.conexao.commit()
        c.close()