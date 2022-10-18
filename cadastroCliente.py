from tkinter import *
from tkinter import ttk
from reportlab.pdfgen import canvas
from PIL import ImageTk, Image
import subsample
import webbrowser
import sqlite3

janelafundo = Tk()

#Gerar relatórios
class Relatorios:
    #Montar relatório
    def rel_geral_cliente(self):
        self.relatorio = canvas.Canvas('C:/ds_python/cadastro_cliente/Relatórios/rel_geral_cliente.pdf')

        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.rgRel = self.rg_entry.get()
        self.emailRel = self.email_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.enderecoRel = self.endereco_entry.get()

        #Cabeçalho
        self.relatorio.setFont('Helvetica-Bold', 16)
        self.relatorio.drawString(200, 790, 'Relatório - Dados Gerais Cliente')

        #Código cliente
        self.relatorio.setFont('Helvetica-Bold', 12)
        self.relatorio.drawString(40, 750, 'Código: ')
        self.relatorio.setFont('Helvetica', 12)
        self.relatorio.drawString(90, 750, self.codigoRel)

        #Nome cliente
        self.relatorio.setFont('Helvetica-Bold', 12)
        self.relatorio.drawString(40, 730, 'Nome: ')
        self.relatorio.setFont('Helvetica', 12)
        self.relatorio.drawString(80, 730, self.nomeRel)

        #Rg cliente
        self.relatorio.setFont('Helvetica-Bold', 12)
        self.relatorio.drawString(40, 710, 'Rg: ')
        self.relatorio.setFont('Helvetica', 12)
        self.relatorio.drawString(63, 710, self.rgRel)

        #Email cliente
        self.relatorio.setFont('Helvetica-Bold', 12)
        self.relatorio.drawString(40, 690, 'Email: ')
        self.relatorio.setFont('Helvetica', 12)
        self.relatorio.drawString(80, 690, self.emailRel)

        #Telefone cliente
        self.relatorio.setFont('Helvetica-Bold', 12)
        self.relatorio.drawString(40, 670, 'Telefone: ')
        self.relatorio.setFont('Helvetica', 12)
        self.relatorio.drawString(95, 670, self.telefoneRel)

        #Endereço cliente
        self.relatorio.setFont('Helvetica-Bold', 12)
        self.relatorio.drawString(40, 650, 'Endereço: ')
        self.relatorio.setFont('Helvetica', 12)
        self.relatorio.drawString(102, 650, self.enderecoRel)

        self.relatorio.rect(20, 630, 550, 190, fill=FALSE, stroke=True)
        self.relatorio.showPage()
        self.relatorio.save()
        self.mostrar_rel()

    #Mostar relatório
    def mostrar_rel(self):
        webbrowser.open('C:/ds_python/cadastro_cliente/Relatórios/rel_geral_cliente.pdf')

#Função dos botões
class FuncoesBotoes:
    #Função Botão Limpar
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.rg_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.endereco_entry.delete(0, END)

    #Conectando ao banco de dados
    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')

    #Desconectando ao banco de dados
    def desconecta_bd(self):
        self.conn.close(); print('Desconectando do banco de dados')

    #Modelagem do Banco de Dados
    def montar_banco(self):
        self.conecta_bd()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTEGER PRIMARY KEY,
                nome CHAR(80) NOT NULL,
                rg INTEGER(9) NOT NULL,
                email CHAR(40) NOT NULL,
                telefone INTEGER(11) NOT NULL,
                endereco CHAR(150) NOT NULL      
            );    
        ''')
        self.conn.commit(); print('Banco de dados criado com sucesso!')
        self.desconecta_bd()

    #Variaveis de busca dos campos do cadastro
    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.rg = self.rg_entry.get()
        self.email = self.email_entry.get()
        self.telefone = self.telefone_entry.get()
        self.endereco = self.endereco_entry.get()

    #Salvando clientes no banco de dados
    def add_clientes(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute('''
        INSERT INTO clientes (nome, rg, email, telefone, endereco)
        VALUES (?, ?, ?, ?, ?)''', (self.nome, self.rg, self.email, self.telefone, self.endereco))
        self.conn.commit()
        self.desconecta_bd()
        self.visualiza_lista()
        self.limpa_tela()

    #Mostrar lista no frame2
    def visualiza_lista(self):
        self.lista_frame2.delete(*self.lista_frame2.get_children())
        self.conecta_bd()
        lista = self.cursor.execute('''SELECT cod, nome, rg, email, telefone, endereco FROM clientes
                                    ORDER BY nome ASC;''')
        for i in lista:
            self.lista_frame2.insert('', END, values=i)
        self.desconecta_bd()

    #Habilitar a função duplo clique
    def duplo_clique(self, event):
        self.limpa_tela()
        self.lista_frame2.selection()

        for n in self.lista_frame2.selection():
            col1, col2, col3, col4, col5, col6 = self.lista_frame2.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.rg_entry.insert(END, col3)
            self.email_entry.insert(END, col4)
            self.telefone_entry.insert(END, col5)
            self.endereco_entry.insert(END, col6)

    #Deletando os registros no banco de dados
    def deletar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(''' DELETE FROM clientes WHERE cod = ? ''', (self.codigo,))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.visualiza_lista()

    #Alterando os registros no banco de dados
    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(''' UPDATE clientes SET nome = ?, rg = ?, email = ?, telefone = ?, endereco = ? 
                            WHERE cod = ? ''', (self.nome, self.rg, self.email, self.telefone, self.endereco, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.visualiza_lista()

    #Buscando os registros no banco de dados
    def buscar_cliente(self):
        self.conecta_bd()
        self.lista_frame2.delete(*self.lista_frame2.get_children())
        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(''' SELECT cod, nome, rg, email, telefone, endereco FROM clientes
                            WHERE nome LIKE "%s" ORDER BY nome ASC ''' %nome)
        buscaCliente = self.cursor.fetchall()

        for n in buscaCliente:
            self.lista_frame2.insert("", END, values= n)

        self.limpa_tela()
        self.desconecta_bd()

class TelaPrincipal(FuncoesBotoes, Relatorios):
    def __init__(self):
        self.janelafundo = janelafundo
        self.tela()
        self.frames_da_tela()
        self.criar_botoes()
        self.criando_labels_entrys()
        self.lista_clientes()
        self.montar_banco()
        self.visualiza_lista()
        self.barra_menu()
        self.imagemlogo()
        janelafundo.mainloop()

    def tela(self):
        self.janelafundo.title('Cadastro de Clientes')
        self.janelafundo.configure(background='#012E40')
        self.janelafundo.geometry('850x680+240+10')
        self.janelafundo.iconbitmap(default='Imagens/icon.ico')
        self.janelafundo.resizable(False, False)
        #self.janelafundo.attributes('-fullscreen', True)
        #self.janelafundo.maxsize(width=1000, height=800)
        #self.janelafundo.minsize(width=900, height=700)

    def imagemlogo(self):
        self.logo = PhotoImage(file='Imagens/LOGO (2).png')
        self.logo = self.logo.subsample(6, 6)
        Label(self.frame_1, image=self.logo, bg='#faf6f2').place(relx=0.15, rely=0.06, relheight=0.2, relwidth=0.2)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.janelafundo, bg='#faf6f2', highlightthickness=3, highlightbackground='#026773')
        self.frame_1.place(relx=0.02, rely=0.02, relheight=0.46, relwidth=0.96)

        self.frame_2 = Frame(self.janelafundo, bg='#faf6f2', highlightthickness=3, highlightbackground='#026773')
        self.frame_2.place(relx=0.02, rely=0.51, relheight=0.46, relwidth=0.96)

    def criar_botoes(self):
        #Botão Limpar
        self.bt_limpar = PhotoImage(file='Imagens/Limpar (2).png')
        #self.bt_limpar = self.bt_limpar.subsample(1, 1)
        self.limpar = Button(self.frame_1, image=self.bt_limpar, command=self.limpa_tela, border=0, highlightthickness=0)
        self.limpar.place(relx=0.36, rely=0.11, relheight=0.1, relwidth=0.11)

        #Botão Buscar
        self.bt_buscar = PhotoImage(file='Imagens/Buscar (1).png')
        self.buscar = Button(self.frame_1, image=self.bt_buscar, command=self.buscar_cliente, border=0, highlightthickness=0)
        self.buscar.place(relx=0.48, rely=0.11, relheight=0.1, relwidth=0.11)

        #Botão Novo
        self.bt_novo = PhotoImage(file='Imagens/Novo (1).png')
        self.novo = Button(self.frame_1, image=self.bt_novo, command=self.add_clientes, border=0, highlightthickness=0)
        self.novo.place(relx=0.6, rely=0.11, relheight=0.1, relwidth=0.11)

        #Botão Alterar
        self.bt_alterar = PhotoImage(file='Imagens/Alterar (1).png')
        self.alterar = Button(self.frame_1, image=self.bt_alterar, command=self.alterar_cliente, border=0, highlightthickness=0)
        self.alterar.place(relx=0.72, rely=0.11, relheight=0.1, relwidth=0.11)

        #Botão Apagar
        self.bt_apagar = PhotoImage(file='Imagens/Apagar (1).png')
        self.apagar = Button(self.frame_1, image=self.bt_apagar, command=self.deletar_cliente, border=0, highlightthickness=0)
        self.apagar.place(relx=0.84, rely=0.11, relheight=0.1, relwidth=0.11)

    def criando_labels_entrys(self): #Criação da legenda e das caixas de texto
        #Label Código
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#faf6f2', fg="black", font=('Verdana', 9, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.29)
        #Posicionamento label código
        self.codigo_entry = Entry(self.frame_1, fg="blue", font=('Verdana', 9, 'bold'), highlightthickness=1, highlightbackground='#026773')
        self.codigo_entry.place(relx=0.05, rely=0.35, relheight=0.08, relwidth=0.12)

        #Label Nome
        self.lb_nome = Label(self.frame_1, text='Nome', bg='#faf6f2', fg="black", font=('Verdana', 9, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.45)
        # Posicionamento label nome
        self.nome_entry = Entry(self.frame_1, fg="blue", font=('Verdana', 10), highlightthickness=1, highlightbackground='#026773')
        self.nome_entry.place(relx=0.05, rely=0.51, relheight=0.08, relwidth=0.44)

        #Label Rg
        self.lb_rg = Label(self.frame_1, text='RG', bg='#faf6f2', fg="black", font=('Verdana', 9, 'bold'))
        self.lb_rg.place(relx=0.51, rely=0.45)
        # Posicionamento label rg
        self.rg_entry = Entry(self.frame_1, fg="blue", font=('Verdana', 10), highlightthickness=1, highlightbackground='#026773')
        self.rg_entry.place(relx=0.51, rely=0.51, relheight=0.08, relwidth=0.44)

        #Label Email
        self.lb_email = Label(self.frame_1, text='E-mail', bg='#faf6f2', fg="black", font=('Verdana', 9, 'bold'))
        self.lb_email.place(relx=0.05, rely=0.62)
        # Posicionamento label código email
        self.email_entry = Entry(self.frame_1, fg="blue", font=('Verdana', 10), highlightthickness=1, highlightbackground='#026773')
        self.email_entry.place(relx=0.05, rely=0.68, relheight=0.08, relwidth=0.44)

        #Label Telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#faf6f2', fg="black", font=('Verdana', 9, 'bold'))
        self.lb_telefone.place(relx=0.51, rely=0.62)
        # Posicionamento label código telefone
        self.telefone_entry = Entry(self.frame_1, fg="blue", font=('Verdana', 10), highlightthickness=1, highlightbackground='#026773')
        self.telefone_entry.place(relx=0.51, rely=0.68, relheight=0.08, relwidth=0.44)

        #Label Endereço
        self.lb_endereco = Label(self.frame_1, text='Endereço', bg='#faf6f2', fg="black", font=('Verdana', 9, 'bold'))
        self.lb_endereco.place(relx=0.05, rely=0.79)
        # Posicionamento label endereço
        self.endereco_entry = Entry(self.frame_1, fg="blue", font=('Verdana', 10), highlightthickness=1, highlightbackground='#026773')
        self.endereco_entry.place(relx=0.05, rely=0.85, relheight=0.08, relwidth=0.9)

    def lista_clientes(self):
        self.lista_frame2 = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.lista_frame2.heading('#1', text='Código')
        self.lista_frame2.heading('#2', text='Nome')
        self.lista_frame2.heading('#3', text='RG')
        self.lista_frame2.heading('#4', text='E-mail')
        self.lista_frame2.heading('#5', text='Telefone')
        self.lista_frame2.heading('#6', text='Endereco')

        self.lista_frame2.column('#0', width=1, anchor=CENTER)
        self.lista_frame2.column('#1', width=30, anchor=CENTER)
        self.lista_frame2.column('#2', width=69, anchor=CENTER)
        self.lista_frame2.column('#3', width=70, anchor=CENTER)
        self.lista_frame2.column('#4', width=70, anchor=CENTER)
        self.lista_frame2.column('#5', width=60, anchor=CENTER)
        self.lista_frame2.column('#6', width=100, anchor=CENTER)

        self.lista_frame2.place(relx=0.05, rely=0.03, relheight=0.94, relwidth=0.9)

        #Adicionar barra de rolagem
        self.barra_rolagem = Scrollbar(self.frame_2, orient='vertical')
        self.lista_frame2.configure(yscrollcommand=self.barra_rolagem.set)
        self.barra_rolagem.place(relx=0.95, rely=0.03, relheight=0.94, relwidth=0.03)

        self.lista_frame2.bind('<Double-1>', self.duplo_clique)

    def barra_menu(self):
        barraMenu = Menu(self.janelafundo)
        self.janelafundo.config(menu=barraMenu)

        colMenu1 = Menu(barraMenu, tearoff=0)
        colMenu2 = Menu(barraMenu, tearoff=0)

        barraMenu.add_cascade(label='Opções', menu=colMenu1)
        barraMenu.add_cascade(label='Relatórios', command=self.rel_geral_cliente)
        barraMenu.add_cascade(label='Encerrar', command=self.sair)

        colMenu1.add_command(label='Adicionar Cliente', command=self.add_clientes)
        colMenu1.add_command(label='Alterar Cliente', command=self.alterar_cliente)
        colMenu1.add_command(label='Apagar Cliente', command=self.deletar_cliente)
        colMenu1.add_command(label='Buscar Cliente', command=self.buscar_cliente)
        colMenu1.add_command(label='Limpar Tela', command=self.limpa_tela)

    def sair(self):
        self.janelafundo.destroy()

TelaPrincipal()