from tkcalendar import Calendar
from datetime import date
from tkinter import Tk, NO, ttk
from customtkinter import CTkLabel, CTkButton, CTkEntry, CTkFrame, CTkOptionMenu, CTkScrollableFrame
import customtkinter
import self as self

from controllers.Pedidos import Pedido
from controllers.Doces import Doce
from controllers.Clientes import Cliente


class Home:

    def __init__(self):

        # Config da janela

        self.data = date.today()
        self.contData = 0

        self.root = customtkinter.CTk()
        self.root.title('ADMIN')

        self.largura = 1280
        self.altura = 600

        # Config da frame
        self.frame = CTkFrame(self.root)
        self.frame.place(x=15, y=100)

        self.root.title('Cadastro de produtos')

        self.root.geometry('1280x720')
        self.root.minsize(950, 500)

        CTkLabel(self.root, text='CandyApp 🧁', font=('Arial', 20)) \
            .grid(row=1, column=1, padx=25, pady=25)

        # Menu
        CTkButton(self.root, text='Home', width=20, hover_color='#fd7066', text_color='white',
                  fg_color='#ff8a82', command=lambda: Home.FrameHome(self, self.root)) \
            .grid(row=1, column=2, padx=10, pady=10)
        CTkButton(self.root, text='Clientes', width=20, hover_color='#fd7066', text_color='white',
                  fg_color='#ff8a82', command=lambda: Home.FrameClientes(self, self.root)) \
            .grid(row=1, column=3, padx=10, pady=10)
        CTkButton(self.root, text='Pedidos', width=20, hover_color='#fd7066', text_color='white',
                  fg_color='#ff8a82', command=lambda: Home.FramePedidos(self, self.root)) \
            .grid(row=1, column=4, padx=10, pady=10)
        CTkButton(self.root, text='Doces', width=20, hover_color='#fd7066', text_color='white',
                  fg_color='#ff8a82', command=lambda: Home.FrameDoces(self, self.root)) \
            .grid(row=1, column=5, padx=10, pady=10)

        Home.FrameHome(self, self.root)

        self.root.mainloop()

    def Calendario(self):

        # Config
        self.calendario = Tk()
        self.calendario.title('Calendário')

        dataAtual = str(date.today()).split('-')

        # Calendar config

        cal = Calendar(self.calendario,
                       selectmode='day',
                       year=int(dataAtual[0]),
                       month=int(dataAtual[1]),
                       day=int(dataAtual[2]))

        cal.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

        # Date formatting

        def pegaData():
            self.data = cal.get_date()

            dataFormatado = str(self.data).split('/')

            ano = dataFormatado[2]
            dia = dataFormatado[1]
            mes = dataFormatado[0]

            dataFormatada = ano + '/' + mes + '/' + dia

            self.data = dataFormatada

            self.calendario.destroy()

            self.contData += 1

        # Date config

        def limpaData():
            self.data = ""
            self.calendario.destroy()

        CTkButton(self.calendario, text='Confirmar', width=20, command=pegaData) \
            .grid(row=1, column=1, columnspan=2, pady=20, padx=10)

        CTkButton(self.calendario, text='Limpar data', width=20, command=limpaData) \
            .grid(row=1, column=2, columnspan=2, pady=25, padx=10)

    def FrameDoces(self, tela):

        # Screen config

        self.root = tela

        try:
            self.frame.destroy()
        except:
            pass

        self.frame = CTkFrame(self.root)
        self.frame.place(x=25, y=100)

        # Titles

        self.root.title('Cadastro de doce')

        CTkLabel(self.frame, text='Cadastro de doce', font=('Arial', 19)).grid(row=5, column=0, columnspan=4, padx=15,
                                                                               pady=6, ipady=15)

        # Buttons and inputs

        # Name
        CTkLabel(self.frame, text='Nome').grid(row=6, column=0, columnspan=1, pady=5, padx=5)
        self.nome = CTkEntry(self.frame)
        self.nome.grid(row=6, column=1, padx=5, pady=5)

        # Ingredients
        CTkLabel(self.frame, text='Ingredientes').grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.ingredientes = CTkEntry(self.frame)
        self.ingredientes.grid(row=7, column=1, padx=5, pady=5)

        # Groups
        CTkLabel(self.frame, text='Grupo').grid(row=8, column=0, columnspan=1, pady=5, padx=5)
        self.grupo = CTkEntry(self.frame)
        self.grupo.grid(row=8, column=1, padx=5, pady=5)

        # Price
        CTkLabel(self.frame, text='Preço').grid(row=9, column=0, columnspan=1, pady=5, padx=5)
        self.preco = CTkEntry(self.frame)
        self.preco.grid(row=9, column=1, padx=5, pady=5)

        CTkButton(self.frame, text='Cadastrar', width=15, fg_color="#64c23b",
                  command=lambda: Doce.Cadastrar(self)).grid(row=12, column=0, padx=15, pady=7)

        CTkButton(self.frame, text='Excluir', width=15, fg_color="#ea6960", hover_color="ea6990",
                  command=lambda: Doce.Remover(self)).grid(row=12, column=1, padx=0, pady=0)

        CTkButton(self.frame, text='Atualizar', width=15, fg_color="#7575fc",
                  command=lambda: Doce.CarregarDados(self)).grid(row=13, column=0, padx=15, pady=17)

        # Table

        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3", "c4"),
                                 show="headings")

        self.tree.configure()

        self.tree.column("c1", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Ingredientes')

        self.tree.column("c3", width=150, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Grupo')

        self.tree.column("c4", width=150, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Preço')

        self.tree.grid(row=6, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        Doce.CarregarDados(self)

        self.root.mainloop()

    def FrameClientes(self, tela):

        # Screen config

        self.root = tela

        try:
            self.frame.destroy()
        except:
            pass

        self.frame = CTkFrame(self.root)
        self.frame.place(x=25, y=100)

        # Titles

        self.root.title('Cadastro de clientes')

        CTkLabel(self.frame, text='Cadastro de clientes', font=('Arial', 19)).grid(row=5, column=0, columnspan=4,
                                                                                   padx=15,
                                                                                   pady=6, ipady=15)

        # Buttons and inputs

        # Name
        CTkLabel(self.frame, text='Nome').grid(row=6, column=0, columnspan=1, pady=5, padx=5)
        self.nome = CTkEntry(self.frame)
        self.nome.grid(row=6, column=1, padx=5, pady=5)

        # Addres
        CTkLabel(self.frame, text='Endereco').grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.endereco = CTkEntry(self.frame)
        self.endereco.grid(row=7, column=1, padx=5, pady=5)

        # Phone
        CTkLabel(self.frame, text='Telefone').grid(row=8, column=0, columnspan=1, pady=5, padx=5)
        self.telefone = CTkEntry(self.frame)
        self.telefone.grid(row=8, column=1, padx=5, pady=5)

        CTkButton(self.frame, text='Cadastrar', width=15, fg_color="#64c23b",
                  command=lambda: Cliente.Cadastrar(self)).grid(row=12, column=0, padx=15, pady=7)

        CTkButton(self.frame, text='Excluir', width=15, fg_color="#ea6960", hover_color="ea6990",
                  command=lambda: Cliente.Remover(self)).grid(row=12, column=1, padx=0, pady=0)

        CTkButton(self.frame, text='Atualizar', width=15, fg_color="#7575fc",
                  command=lambda: Cliente.CarregarDados(self)).grid(row=13, column=0, padx=15, pady=17)

        # Table

        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3"),
                                 show="headings")

        self.tree.configure()

        self.tree.column("c1", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=350, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Endereco')

        self.tree.column("c3", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Telefone')

        self.tree.grid(row=6, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        Cliente.CarregarDados(self)

        self.root.mainloop()

    def FramePedidos(self, tela):

        # Screen config

        self.root = tela

        try:
            self.frame.destroy()
        except:
            pass

        self.frame = CTkFrame(self.root)
        self.frame.place(x=25, y=100)

        # Titles
        self.root.title('Pedidos')
        CTkLabel(self.frame, text='Cadastro de Pedidos', font=('Arial', 19)) \
            .grid(row=5, column=0, columnspan=4, padx=15, pady=5, ipady=15)

        # Buttons and inputs

        # Date
        CTkLabel(self.frame, text='Data de entrega') \
            .grid(row=6, column=0, columnspan=1, pady=0, padx=0)
        self.data_entrega = CTkButton(self.frame, text='Selecionar data', command=lambda: Home.Calendario(self))
        self.data_entrega.grid(row=6, column=1, padx=0, pady=0)

        # Name
        CTkLabel(self.frame, text='Nome cliente')\
            .grid(row=7, column=0, columnspan=1, pady=5, padx=5)
        self.cliente = CTkEntry(self.frame)
        self.cliente.grid(row=7, column=1, padx=5, pady=5)

        # Candy
        CTkLabel(self.frame, text='Doce')\
            .grid(row=8, column=0, columnspan=1, pady=5, padx=5)
        self.doce = CTkOptionMenu(self.frame, values=Doce.Nomes(self), dynamic_resizing=False)
        self.doce.grid(row=8, column=1, padx=5, pady=5)

        # Amount
        CTkLabel(self.frame, text='Quantidade')\
            .grid(row=9, column=0, columnspan=1, pady=5, padx=5)
        self.quantidade = CTkEntry(self.frame)
        self.quantidade.grid(row=9, column=1, padx=5, pady=5)

        CTkButton(self.frame, text='Cadastrar', width=15, fg_color="#64c23b",
                  command=lambda: Pedido.Cadastrar(self)).grid(row=12, column=0, padx=15, pady=7)

        CTkButton(self.frame, text='Excluir', width=15, fg_color="#ea6960", hover_color="ea6990",
                  command=lambda: Pedido.Remover(self)).grid(row=12, column=1, padx=0, pady=0)

        CTkButton(self.frame, text='Atualizar', width=15, fg_color="#7575fc",
                  command=lambda: Pedido.CarregarDados(self)).grid(row=14, column=0, padx=15, pady=17)

        # Table

        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),
                                 show="headings")

        self.tree.configure()

        self.tree.column("c1", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Endereco')

        self.tree.column("c3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Telefone')

        self.tree.column("c4", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Doce')

        self.tree.column("c5", width=70, minwidth=500, stretch=NO)
        self.tree.heading('#5', text='Quantidade')

        self.tree.column("c6", width=50, minwidth=500, stretch=NO)
        self.tree.heading('#6', text='Valor')

        self.tree.column("c7", width=75, minwidth=500, stretch=NO)
        self.tree.heading('#7', text='Entrega')

        self.tree.grid(row=6, column=5, padx=10, pady=10, columnspan=3, rowspan=6)

        Pedido.CarregarDados(self)

        self.root.mainloop()

    def FrameHome(self, tela):

        # Screen config

        self.root = tela

        try:
            self.frame.destroy()
            self.frame_title.destroy()
        except:
            pass

        # Titles

        self.frame_title = CTkFrame(self.root)
        self.frame_title.place(x=25, y=100)

        # Update text on screen
        def updateTextTitle():

            # Destroy component
            self.frame_title.destroy()

            # Recreate component

            self.frame_title = CTkFrame(self.root)
            self.frame_title.place(x=25, y=100)

            if self.contData == 0:
                textTitle = "Pedidos do dia"
            elif self.data != "":

                dataFormatado = str(self.data).split('/')

                ano = dataFormatado[0]
                dia = dataFormatado[2]
                mes = dataFormatado[1]

                if len(dia) == 1:
                    dia = "0" + dia
                if len(mes) == 1:
                    mes = "0" + mes

                dataFormatada = dia + '/' + mes + '/' + "20" + ano

                textTitle = "Pedidos do dia: " + str(dataFormatada)
            else:
                textTitle = "Pedidos do dia"

            # Print text
            CTkLabel(self.frame_title, text=textTitle, font=('Arial', 30)) \
                .grid(row=1, column=0, columnspan=4, padx=15, pady=6, ipady=15)

        updateTextTitle()

        self.frame = CTkFrame(self.root)
        self.frame.place(x=25, y=200)

        # Filter
        self.frame_filter = CTkFrame(self.root)
        self.frame_filter.place(x=25, y=470)

        # Title
        self.root.title('CandyApp')

        # Information
        self.tree = ttk.Treeview(self.frame, selectmode="browse", columns=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),
                                 show="headings")

        # Table

        self.tree.configure()

        self.tree.column("c1", width=170, minwidth=500, stretch=NO)
        self.tree.heading('#1', text='Nome')

        self.tree.column("c2", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#2', text='Endereco')

        self.tree.column("c3", width=100, minwidth=500, stretch=NO)
        self.tree.heading('#3', text='Telefone')

        self.tree.column("c4", width=200, minwidth=500, stretch=NO)
        self.tree.heading('#4', text='Doce')

        self.tree.column("c5", width=70, minwidth=500, stretch=NO)
        self.tree.heading('#5', text='Quantidade')

        self.tree.column("c6", width=50, minwidth=500, stretch=NO)
        self.tree.heading('#6', text='Valor')

        self.tree.column("c7", width=75, minwidth=500, stretch=NO)
        self.tree.heading('#7', text='Entrega')

        self.tree.grid(row=2, column=1, padx=10, pady=10, columnspan=3, rowspan=6)

        # Filters

        self.filtrar = CTkButton(self.frame_filter, text='Filtrar', fg_color="#64c23b",
                                 command=lambda: [Pedido.CarregarDadosFiltro(self), updateTextTitle()])
        self.filtrar.grid(row=0, column=1, padx=5, pady=5)

        # Clean filter
        self.filtrar = CTkButton(self.frame_filter, text='Cancelar Pedido', fg_color="#FF4E28", hover_color="#FF2F02",
                                 command=lambda: [Pedido.Remover(self), Pedido.CarregarDadosFiltro(self)])
        self.filtrar.grid(row=0, column=2, padx=5, pady=5)

        # Date
        self.data_entrega_filtro = CTkButton(self.frame_filter, text='Selecionar data',
                                             command=lambda: Home.Calendario(self))
        self.data_entrega_filtro.grid(row=0, column=3, padx=5, pady=5)

        ListaCliente = Cliente.CarregarNomes(self)
        ListaCliente.append('Nenhum')

        optionmenu_var_doce = customtkinter.StringVar(value="Doces")

        # Client
        self.cliente_filtro = CTkEntry(self.frame_filter, placeholder_text="Nome do cliente")
        self.cliente_filtro.grid(row=0, column=4, padx=5, pady=5)

        ListaDoce = Doce.Nomes(self)
        ListaDoce.append('Doces')

        # Candy
        self.doce_filtro = CTkOptionMenu(self.frame_filter, values=ListaDoce, dynamic_resizing=False,
                                         variable=optionmenu_var_doce)
        self.doce_filtro.grid(row=0, column=5, padx=5, pady=5)

        Pedido.CarregarDadosFiltro(self)

        self.root.mainloop()