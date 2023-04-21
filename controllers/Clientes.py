from tkinter import *
from tkinter import messagebox

from self import self

from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert
import pandas as pd


class Cliente:

    def __init__(self):
        Cliente.CarregarDados(self)
        nome = ''
        endereco = ''
        telefone = ''

    def Cadastrar(self):

        nome = self.nome.get()
        endereco = self.endereco.get()
        telefone = self.telefone.get()

        Insert.InsereCliente(self, nome, endereco, telefone)

        Cliente.CarregarDados(self)

    def CarregarDados(self):

        resultados = Consulta.Clientes(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])
            linhaV.append(linha['endereco'])
            linhaV.append(linha['telefone'])

            self.tree.insert('', END, values=linhaV, iid=linha['id_cliente'], tag='1')

            linhaV.clear()

    def Remover(self):

        id_cliente = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'CLIENTES', 'ID_CLIENTE', id_cliente)
        Cliente.CarregarDados(self)

    def CarregarNomes(self):

        resultados = Consulta.Clientes(self)

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])

        return linhaV