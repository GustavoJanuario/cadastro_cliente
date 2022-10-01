from tkinter import *

######    FUNÇÕES    #####
def verifica_usuario():
    lbl_print['text'] = 'Seu usuário é:' + str()


######    INTERFACE GRAFICA    #####

janela_principal = Tk()
janela_principal.title('Cadastro de Clientes')


######    COMPONENTES    #####
lbl_usuario = Label(janela_principal, text='Digite seu usuário: ')
caixa_usuario = Entry(janela_principal)
lbl_senha = Label(janela_principal, text='Digite sua Senha: ')
caixa_senha = Entry(janela_principal)
btn_entrar = Button(janela_principal, text='Entrar', command=verifica_usuario)
lbl_print = Label(janela_principal, text='Seu usuario é: ')

######    POSIÇÃO DOS COMPONENTES(LAYOUT)    #####
lbl_usuario.grid()
caixa_usuario.grid()
lbl_senha.grid()
caixa_senha.grid()
btn_entrar.grid()
lbl_print.grid()

janela_principal.mainloop()