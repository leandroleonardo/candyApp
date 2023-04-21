from tkinter import *
from tkinter import messagebox

from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert
import pandas as pd


class Doce:

    def __init__(self):
        nome = ''
        ingrediente = ''
        grupo = ''
        preco = ''

    def Cadastrar(self):

        nome = self.nome.get()
        ingredientes = self.ingredientes.get()
        grupo = self.grupo.get()
        preco = self.preco.get()

        Insert.InsereDoce(self, nome, ingredientes, grupo, preco)

        Doce.CarregarDados(self)

    def CarregarDados(self):

        resultados = Consulta.Doces(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['ingredientes'])
            linhaV.append(linha['grupo'])
            linhaV.append(linha['preco'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_doce'], tag='1')

            linhaV.clear()

    def Remover(self):

        id_doce = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'DOCES', 'ID_DOCE', id_doce)
        Doce.CarregarDados(self)

    def Nomes(self):

        resultados = Consulta.Doces(self)

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])

        return linhaV