from tkinter import *
from tkinter import ttk

janelalogin = Tk()
estilottk = ttk

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
        self.username = ttk.Entry(self.janelalogin, font='Helvetica, 12',)
        #self.username.configure(border=2, font='Helvetica, 12', fg="black")
        self.username.place(relx=0.5, rely=0.47, relheight=0.08, relwidth=0.4)
        self.username.focus_set()

        self.password = ttk.Entry(self.janelalogin, font='Helvetica, 13', show='•')
        #self.password.configure(border=2, show='*', font='Helvetica, 13', fg="black")
        self.password.place(relx=0.5, rely=0.64, relheight=0.08, relwidth=0.4)
        self.username.focus_set()

    def Botoes(self):
        self.btn_login = Button(self.janelalogin, text='Entrar', bg='#C9E7F1', font=('Helvetica', 11, 'bold'))
        self.btn_login.place(relx=0.72, rely=0.78, relheight=0.08, relwidth=0.18)

        self.btn_cadastro = Button(self.janelalogin, text='Cadastre-se', command=self.CadastrarUsuario, bg='#C9E7F1', font=('Helvetica', 11, 'bold'))
        self.btn_cadastro.place(relx=0.5, rely=0.78, relheight=0.08, relwidth=0.18)

    def CadastrarUsuario(self):
        #Removendo os botões
        self.btn_login.place(x=610)
        self.btn_cadastro.place(x=610)

        #Inserindo os novos campos
        self.nomecadastro

    def EstiloTtk(self):
        self.username.configure()

TelaPrincipal()
