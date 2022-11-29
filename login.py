from tkinter import *

######    FUNÇÕES    #####

def verifica_usuario():
    usuario = caixa_usuario.get()
    senha = caixa_senha.get()

    if usuario == 'admin' and senha == '123456':
        lbl_verifica = Label(janela_principal, text='Bem vindo!')
        lbl_verifica.place(relx=0.3, rely=0.88, relheight=0.1, relwidth=0.4)
        limpa_tela()
    else:
        lbl_verifica = Label(janela_principal, text='Usuário ou senha incorretos!')
        lbl_verifica.grid(row=4, column=1)
        limpa_tela()

def limpa_tela():
    caixa_usuario.delete(0, END)
    caixa_senha.delete(0, END)


######    INTERFACE GRAFICA    #####

janela_principal = Tk()
janela_principal.title('Login')
janela_principal.geometry('300x400+500+153')
janela_principal.iconbitmap(default='Imagens/icon.ico')
janela_principal.resizable(False, False)
bg = PhotoImage(file='Imagens/fundo_login.png')
label1 = Label(janela_principal, image=bg, border=0, highlightthickness=0)
label1.place(x=0, y=0)
logo = PhotoImage(file='Imagens/LOGO (2).png').subsample(5, 5)
label2 = Label(janela_principal, image=logo).place(relx=0.35, rely=0.01)



######    COMPONENTES    #####
lbl_usuario = Label(janela_principal, text='Usuário', font=('Verdana', 10, 'bold'), background='#ffffff')
caixa_usuario = Entry(janela_principal, font=('Verdana', 9))
lbl_senha = Label(janela_principal, text='Senha', font=('Verdana', 10, 'bold'), background='#026773')
caixa_senha = Entry(janela_principal, show='*', font=('Verdana', 9))
btn_entrar = Button(janela_principal, text='ENTRAR', command=verifica_usuario, font=('Verdana', 10))
lbl_verifica = Label(janela_principal, text='')


######    POSIÇÃO DOS COMPONENTES(LAYOUT)    #####
lbl_usuario.place(relx=0.1, rely=0.32, relheight=0.06, relwidth=0.19)
caixa_usuario.place(relx=0.1, rely=0.40, relheight=0.08, relwidth=0.8)
lbl_senha.place(relx=0.1, rely=0.52, relheight=0.08, relwidth=0.15)
caixa_senha.place(relx=0.1, rely=0.61, relheight=0.08, relwidth=0.8)
btn_entrar.place(relx=0.4, rely=0.78, relheight=0.08, relwidth=0.2)


janela_principal.mainloop()