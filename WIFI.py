from time import sleep

# Desafio !!
# Desafio 1
""" Voce ira criar um modulo "WIFI" e neste modulo eu quero
que você crie 3 métodos:
    1. Criar rede Wifi
    2. Alterar Senha Wifi 
    3. Conectar a Wifi
Depois de ter criado o modulo com essas funcionalidades,
você devera voltar ao seu arquivo principal, importar o modulo
'WIFI' e usar todos os 3 métodos que você criou"""

""" def criar_wifi():
    nomewifi = str(input("Crie o nome do seu WIFI: "))
    senhawifi = str(input("Crie a senha do seu WIFI: "))

#def alterar_senha_wifi():
    pergunta = str(input("Deseja alterar a senha do seu WIFI: "))
    if pergunta == "sim" or pergunta == "Sim":
        senhawifi = str(input("Digite a nova senha WIFI: "))

#def conectar_wifi():
    print("\n\n######################")
    print("...Conectar ao WIFI...")
    print("######################")
    LoginNome = str(input("Digite o nome do WIFI que deseja conectar: "))
    if LoginNome == nomewifi:
        LoginSenha = str(input(f"Digite a senha do WIFI {LoginNome}: "))
        if LoginSenha == senhawifi:
            print("conectando.")
            sleep(1)
            print("conectando..")
            sleep(1)
            print("conectando...")
            sleep(1)
            print("conectando.")
            sleep(1)
            print("conectando..")
            sleep(1)
            print("conectando...")
            sleep(1)
            print("Conectado com sucesso !!")
        else:
            print("Senha invalida !!")
    else: 
        print("Nome do WIFI inexistente !!") """

def criar_wifi():
    nomewifi = input("Crie um nome para o WIFI: ")
    senhawifi = input("Crie uma senha para o WIFI: ")
    print(f"WIFI criado com sucesso !!\nNome do wifi: {nomewifi}\nSenha do wifi: {senhawifi}")

def mudar_senha_wifi():
    novasenha = input("Digite sua nova senha: ")
    print(f"Senha alterada com sucesso !!\nNova senha: {novasenha}")

def conectar_wifi():
    print("Conectando.")
    sleep(1)
    print("Conectando..")
    sleep(1)
    print("Conectando...")
    sleep(1)
    print("Conectando.")
    sleep(1)
    print("Conectando..")
    sleep(1)
    print("Conectando...")
    sleep(2)
    print("Conectado com sucesso !!")



            
    