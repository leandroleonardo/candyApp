from tkinter import messagebox

from self import self

from models.ConexaoBD import ConexaoBd


class Consulta:

    # Basic Select

    def Tabela(self, nome):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM ' + nome)
                resultados = cursor.fetchall()
        except:
            return

        return resultados

    # Basic Select if parameters

    def TabelaParams(self, tabela, conteudo):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM {} WHERE NOME = "{}"'.format(tabela, conteudo))
                resultados = cursor.fetchall()
        except:
            return

        return resultados

    # Select in the order table

    def Pedidos(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:

                query = 'SELECT ID_PEDIDO, CLIENTES.NOME, CLIENTES.ENDERECO,CLIENTES.TELEFONE, DOCES.NOME, ' \
                        'QUANTIDADE, PRECO_TOTAL,DATE_FORMAT (`DATA_ENTREGA`,"%d/%m/%Y") AS DATA_ENTREGA '\
                        'FROM PEDIDOS INNER JOIN CLIENTES ON PEDIDOS.ID_CLIENTE = CLIENTES.ID_CLIENTE INNER JOIN ' \
                        'DOCES ON PEDIDOS.ID_DOCE = DOCES.ID_DOCE; '

                cursor.execute(query)

                resultados = cursor.fetchall()

                return resultados
        except:
            return

    # Select from formatted products table

    def Doces(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM DOCES')
                resultados = cursor.fetchall()
                return resultados
        except:
            messagebox.showinfo('Erro', 'Erro ao consultar banco de dados')

    # Select in the Clientes table

    def Clientes(self):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM CLIENTES')
                resultados = cursor.fetchall()
                return resultados
        except:
            messagebox.showinfo('Erro', 'Erro ao consultar banco de dados')

    # Select in the FiltroPedidos table

    def FiltroPedidos(self):

        data = ""

        ConexaoBd.AbreConexao(self)

        data = self.data
        cliente = self.cliente_filtro.get()
        doce = self.doce_filtro.get()

        # Monta filtro para Query

        params = 0
        filterQuery = " WHERE "

        if data != "":
            filterQuery += 'DATA_ENTREGA = "{}" '.format(data)
            params += 1
        if cliente != "":
            if params >= 1:
                filterQuery += ' AND CLIENTES.NOME = "{}" '.format(cliente)
            else:
                filterQuery += ' CLIENTES.NOME = "{}" '.format(cliente)
        if doce != "Doces":
            if params >= 1:
                filterQuery += ' AND DOCES.NOME = "{}" '.format(doce)
            else:
                filterQuery += ' DOCES.NOME = "{}" '.format(doce)

        # Monta consulta

        query = 'SELECT ID_PEDIDO, CLIENTES.NOME, CLIENTES.ENDERECO,CLIENTES.TELEFONE, DOCES.NOME, ' \
                'QUANTIDADE, PRECO_TOTAL,DATE_FORMAT (`DATA_ENTREGA`,"%d/%m/%Y") AS DATA_ENTREGA  ' \
                'FROM PEDIDOS INNER JOIN CLIENTES ON PEDIDOS.ID_CLIENTE = CLIENTES.ID_CLIENTE INNER JOIN ' \
                'DOCES ON PEDIDOS.ID_DOCE = DOCES.ID_DOCE '

        if filterQuery != " WHERE ":
            query += filterQuery + ";"

        # Busca dados de pedido no banco de dados

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute(query)
                resultados = cursor.fetchall()
                return resultados
        except:
            Consulta.Pedidos(self)

        Consulta.Pedidos(self)
