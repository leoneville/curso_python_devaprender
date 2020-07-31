#Como Debuggar seu codigo

import random

class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ["Cristian", "Robert", "Rossana", "Ana"]


    def Iniciar(self):
        print("Olá, Bem vindo a este site!") #inicie o debug aqui (coloque um breakpoint)
        self.ChutarIdade(self.pessoas) #pule essa linha
        self.ChutarNome() # Entre dentro do método dessa linha
        self.ChutarCor() # Entre neste metodo
        print("Programa Finalizado")


    def ChutarCor(self):
        cores = ["Azul", "Rosa", "Verde"]
        for cor in cores:
            print(f"as opçoes de cores são: {cor}")

        print("sua cor favorita é...") # Nao continue a execuçao aqui, volte para onde estava antes
        cor_preferida = random.choice(cores)
        print(cor_preferida)

    def ChutarNome(self):
        nome = f'bem vindo {random.choice(self.pessoas)}'
        print(nome)

    
    def ChutarIdade(self, pessoas):
        # Entre aqui
        idade = random.randint(18,50)
        print(idade)

email = EmailDeBoasVindas()
email.Iniciar()

""" class EmailDeBoasVindas:
    def __init__(self):
        self.pessoas = ["Cristian", "Robert", "Rossana", "Ana"]


    def Iniciar(self):
        print("Olá, Bem vindo a este site!")
        emails_apresentacao = self.MontarCredencial(self.pessoas)
        for email in emails_apresentacao:
            print(email)


    def MontarCredencial(self, pessoas):
        credenciais = []
        for pessoa in pessoas:
            credenciais.append(f'A empresa gostaria de dar as boas vindas para o(a) {pessoa}')
        return credenciais

email = EmailDeBoasVindas()
email.Iniciar() """

# "F5" Começar a debuggar seu código
# "F10" Analisar linha sem entrar no código interno
# "F11" Analisar linha e entrar no codigo interno
#"SHIFT - F11" Sair do bloco de codigo atual e continuar a execuçao

        
