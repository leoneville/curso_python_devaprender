usuario = str(input('Qual é o seu usuário? '))
senha = str(input('Qual é a sua senha? '))
def Logar(usuario, senha):
    print('Logado com sucesso!')
    for i in range(len(senha)): # cria um loop percorrendo toda a string 'senha'
        senha = senha.replace(senha[i], '*') # substitui o caractere atual por um '*'
    print(f'Credenciais --- Usuário: {usuario} | Senha: {senha}')
Logar(usuario, senha)