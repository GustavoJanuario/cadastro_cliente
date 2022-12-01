from tkinter import *
from tkinter import ttk

janelalogin = Tk()
estilottk = ttk.Style()

#ttk.Style = ttkstyle()

class TelaPrincipal():
    def __init__(self):
        self.janelalogin = janelalogin
        self.EstruturaTela()
        self.ImagemFundo()
        self.EntradaDados()
        self.Botoes()
        janelalogin.mainloop()

    def EstruturaTela(self):
        self.janelalogin.title('Sistema - Login')
        self.janelalogin.geometry('600x400+500+153')
        self.janelalogin.resizable(False, False)
        self.janelalogin.iconbitmap(default='Imagens/icon.ico')

    def ImagemFundo(self):
        self.imagemfundo = PhotoImage(file='Imagens/Cadastro de clientes (1).png')
        Label(self.janelalogin, image=self.imagemfundo).place(x=0, y=0)

    def EntradaDados(self):
        # Label login
        self.lbl_username = ttk.Label(self.janelalogin)
        self.lbl_username.place(relx=0.5, rely=0.37)
        self.lbl_username.configure(text='Login', font=('Helvetica', 12, 'bold'), background='#f6f6f6',
                                    foreground='#3d9fc9', justify='left')
        # Entry login
        self.username = ttk.Entry(self.janelalogin, font='Helvetica, 12')
        self.username.place(relx=0.5, rely=0.44, relheight=0.08, relwidth=0.4)
        self.username.focus_set()

        # Label senha
        self.lbl_password = ttk.Label(self.janelalogin)
        self.lbl_password.place(relx=0.5, rely=0.55)
        self.lbl_password.configure(text='Senha', font=('Helvetica', 12, 'bold'), background='#f6f6f6',
                                    foreground='#3d9fc9', justify='center')
        # Entry senha
        self.password = ttk.Entry(self.janelalogin, font='Helvetica, 13', show='•')
        self.password.place(relx=0.5, rely=0.62, relheight=0.08, relwidth=0.4)
        self.username.focus_set()

    def Botoes(self):
        self.btn_login = Button(self.janelalogin)
        self.btn_login.configure(text='Entrar', bg='#13c1c7', fg='black', font=('Helvetica', 11, 'bold'))
        self.btn_login.place(relx=0.72, rely=0.78, relheight=0.08, relwidth=0.18)

        self.btn_cadastro = Button(self.janelalogin)
        self.btn_cadastro.configure(text='Cadastre-se', command=self.CadastrarUsuario, bg='#13c1c7',
                                    font=('Helvetica', 11, 'bold'))
        self.btn_cadastro.place(relx=0.5, rely=0.78, relheight=0.08, relwidth=0.18)

    def CadastrarUsuario(self):
        #Removendo campos da tela de login
        self.lbl_username.place(x=610)
        self.username.place(x=610)
        self.lbl_password.place(x=610)
        self.password.place(x=610)
        self.btn_login.place(x=610)
        self.btn_cadastro.place(x=610)

        #Inserindo os novos campos

        # Label Nome Completo
        self.lbl_nome_cadastro = ttk.Label(self.janelalogin)
        self.lbl_nome_cadastro.place(relx=0.5, rely=0.11)
        self.lbl_nome_cadastro.configure(text='Nome Completo', font=('Helvetica', 12, 'bold'),
                                            background='#f6f6f6', foreground='#3d9fc9', justify='left')
        # Entry Nome Completo
        self.nome_cadastro = ttk.Entry(self.janelalogin, font='Helvetica, 12')
        self.nome_cadastro.place(relx=0.5, rely=0.17, relheight=0.08, relwidth=0.4)
        self.nome_cadastro.focus_set()

        # Label Email
        self.lbl_email_cadastro = ttk.Label(self.janelalogin)
        self.lbl_email_cadastro.place(relx=0.5, rely=0.27)
        self.lbl_email_cadastro.configure(text='Email', font=('Helvetica', 12, 'bold'),
                                            background='#f6f6f6', foreground='#3d9fc9', justify='left')
        # Entry Email
        self.email_cadastro = ttk.Entry(self.janelalogin, font='Helvetica, 12')
        self.email_cadastro.place(relx=0.5, rely=0.33, relheight=0.08, relwidth=0.4)

        # Label Login
        self.lbl_login_cadastro = ttk.Label(self.janelalogin)
        self.lbl_login_cadastro.place(relx=0.5, rely=0.43)
        self.lbl_login_cadastro.configure(text='Login', font=('Helvetica', 12, 'bold'),
                                            background='#f6f6f6', foreground='#3d9fc9', justify='left')
        # Entry Login
        self.login_cadastro = ttk.Entry(self.janelalogin, font='Helvetica, 12')
        self.login_cadastro.place(relx=0.5, rely=0.49, relheight=0.08, relwidth=0.4)

        # Label Senha
        self.lbl_senha_cadastro = ttk.Label(self.janelalogin)
        self.lbl_senha_cadastro.place(relx=0.5, rely=0.59)
        self.lbl_senha_cadastro.configure(text='Senha', font=('Helvetica', 12, 'bold'),
                                            background='#f6f6f6', foreground='#3d9fc9', justify='left')
        # Entry Senha
        self.senha_cadastro = ttk.Entry(self.janelalogin, font='Helvetica, 12')
        self.senha_cadastro.place(relx=0.5, rely=0.65, relheight=0.08, relwidth=0.4)

        # Botao voltar
        self.btn_voltar = Button(self.janelalogin)
        self.btn_voltar.configure(text='Voltar', command=self.RetornarTelaPrincipal, bg='#13c1c7',
                                    font=('Helvetica', 11, 'bold'))
        self.btn_voltar.place(relx=0.5, rely=0.78, relheight=0.08, relwidth=0.18)

        # Botao cadastrar
        self.btn_cadastrar = Button(self.janelalogin)
        self.btn_cadastrar.configure(text='Cadastrar', bg='#13c1c7', font=('Helvetica', 11, 'bold'))
        self.btn_cadastrar.place(relx=0.72, rely=0.78, relheight=0.08, relwidth=0.18)

    def RetornarTelaPrincipal(self):

        # Removendo os itens da tela de cadastro
        # Label
        self.lbl_nome_cadastro.place(x=610)
        self.lbl_email_cadastro.place(x=610)
        self.lbl_login_cadastro.place(x=610)
        self.lbl_senha_cadastro.place(x=610)
        # Entry
        self.nome_cadastro.place(x=610)
        self.email_cadastro.place(x=610)
        self.login_cadastro.place(x=610)
        self.senha_cadastro.place(x=610)
        # Button
        self.btn_voltar.place(x=610)
        self.btn_cadastrar.place(x=610)

        # Retorna os itens da tela de login
        self.EntradaDados()
        self.Botoes()


    def EstiloTtk(self):
        self.username.configure()

TelaPrincipal()
