from tkinter import messagebox

import pymysql.cursors

# Opens a database connection


class ConexaoBd:

    def __init__(self):
        self.conexao = None

    def AbreConexao(self):

        try:
            self.conexao = pymysql.connect(
                host='localhost',
                user='root',
                password='root',
                database='candyapp',
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            messagebox.showinfo('Error', 'Erro ao tentar conectar com banco de dados, consulte o suporte.')
            return False


ConexaoBd().AbreConexao()
