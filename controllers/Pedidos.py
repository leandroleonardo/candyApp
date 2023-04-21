from tkinter import *
from tkinter import messagebox

from models.Consulta import Consulta
from models.Delete import Delete
from models.Insert import Insert
import pandas as pd


class Pedido:

    def __init__(self):
        nome = ''
        ingrediente = ''
        grupo = ''
        preco = ''

    def Cadastrar(self):

        nome = self.cliente.get()
        quantidade = int(self.quantidade.get())
        data_entrega = self.data
        doce = self.doce.get()

        Insert.InserePedido(self, nome, quantidade, data_entrega, doce)

        Pedido.CarregarDados(self)

    def CarregarDados(self):

        resultados = Consulta.Pedidos(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['NOME'])
            linhaV.append(linha['ENDERECO'])
            linhaV.append(linha['TELEFONE'])
            linhaV.append(linha['DOCES.NOME'])
            linhaV.append(linha['QUANTIDADE'])
            linhaV.append(linha['PRECO_TOTAL'])
            linhaV.append(linha['DATA_ENTREGA'])

            self.tree.insert('', END, values=linhaV, iid=linha['ID_PEDIDO'], tag='1')

            linhaV.clear()

    def Remover(self):

        id_pedido = int(self.tree.selection()[0])
        Delete.RemoverID(self, 'PEDIDOS', 'ID_PEDIDO', id_pedido)
        Pedido.CarregarDados(self)

    def Nomes(self):

        resultados = Consulta.Doces(self)

        linhaV = []

        for linha in resultados:
            linhaV.append(linha['nome'])

        return linhaV

    def CarregarDadosFiltro(self):

        resultados = Consulta.FiltroPedidos(self)

        self.tree.delete(*self.tree.get_children())

        linhaV = []

        for linha in resultados:

            linhaV.append(linha['NOME'])
            linhaV.append(linha['ENDERECO'])
            linhaV.append(linha['TELEFONE'])
            linhaV.append(linha['DOCES.NOME'])
            linhaV.append(linha['QUANTIDADE'])
            linhaV.append(linha['PRECO_TOTAL'])
            linhaV.append(linha['DATA_ENTREGA'])

            self.tree.insert('', END, values=linhaV, iid=linha['ID_PEDIDO'], tag='1')

            linhaV.clear()
