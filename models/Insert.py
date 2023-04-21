from tkinter import messagebox
from models.ConexaoBD import ConexaoBd


class Insert:

    def InsereVenda(self, id_usuario, id_produto, nome, quantidade, valor_total, data_vendas):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO VENDAS (ID_USUARIO, ID_PRODUTO, NOME, QUANTIDADE, PRECO_TOTAL, '
                               'DATA_VENDA) VALUES ({},{},"{}",{},{},"{}")'.format(id_usuario, id_produto,
                                                                                   nome, quantidade, valor_total,
                                                                                   data_vendas))
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Produto cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao inserir pedido no banco de dados!')

    def InsereDoce(self, nome, ingredientes, grupo, preco):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM DOCES WHERE NOME = %s', nome)
                check = cursor.fetchall()
                if check:
                    messagebox.showinfo('Erro', 'Produto já cadastrado')
                    return
        except:
            pass

        # Insere candy
        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO DOCES (NOME, INGREDIENTES, GRUPO, PRECO)'
                               'VALUES (%s,%s,%s,%s)', (nome, ingredientes, grupo, preco))
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Produto cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao inserir produto no banco de dados')

    def InsereCliente(self, nome, endereco, telefone):

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT * FROM CLIENTES WHERE NOME = %s', nome)
                check = cursor.fetchall()
                if check:
                    messagebox.showinfo('Erro', 'Cliente já cadastrado')
                    return
        except:
            pass

        # Insert client
        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('INSERT INTO CLIENTES (NOME, ENDERECO, TELEFONE)'
                               'VALUES (%s,%s,%s)', (nome, endereco, telefone))
                self.conexao.commit()
                messagebox.showinfo('Mensagem', 'Cliente cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao registrar cliente')

    def InserePedido(self, nome, quantidade, data_entrega, doce):

        # Get ID Cliente

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT ID_CLIENTE FROM CLIENTES WHERE NOME = %s', nome)
                id_cliente = cursor.fetchall()[0]['ID_CLIENTE']
        except:
            pass

        # Get ID Candy

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT ID_DOCE FROM DOCES WHERE NOME = %s', doce)
                id_doce = cursor.fetchall()[0]['ID_DOCE']
        except:
            pass

        # Price Candy

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:
                cursor.execute('SELECT PRECO FROM DOCES WHERE NOME = %s', doce)
                preco = cursor.fetchall()[0]['PRECO']
                preco_total = preco * quantidade
        except:
            pass

        # Insert request

        ConexaoBd.AbreConexao(self)

        try:
            with self.conexao.cursor() as cursor:

                cursor.execute("INSERT INTO PEDIDOS (id_cliente, id_doce, quantidade, preco_total, data_entrega)"
                               "VALUES (%s,%s,%s,%s,%s)", (id_cliente, id_doce, quantidade, preco_total, data_entrega))

                self.conexao.commit()

                messagebox.showinfo('Mensagem', 'Pedido cadastrado com sucesso!')
        except:
            messagebox.showinfo('Erro', 'Erro ao cadastrar pedido')
