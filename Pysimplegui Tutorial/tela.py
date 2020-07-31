#Interface com a biblioteca PySimpleGUI
import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel("DarkBrown4")
        #layout
        layout = [
            [sg.Text("Nome",size=(5,0)),sg.Input(size=(15,0),key="nome")],
            [sg.Text("Idade",size=(5,0)),sg.Input(size=(15,0),key="idade")],
            [sg.Text("Qual o seu email?")],
            [sg.Radio("Gmail","email",key="gmail"),sg.Radio("Hotmail","email",key="hotmail"),sg.Radio("Yahoo","email",key="yahoo"),sg.Radio("Outlook","email",key="outlook")],
            [sg.Text("Aceita cartão?")],
            [sg.Radio("Sim","cartoes",key="aceitaCartao"),sg.Radio("Não","cartoes",key="naoAceitaCartao")],
            [sg.Slider(range=(0,255),default_value=0,orientation="h",size=(15,20),key="sliderVelocidade")],
            [sg.Button("Enviar Dados")],
            [sg.Output(size=(30,20))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usúario").layout(layout)
        #Extrair os dados da tela
        #self.button, self.values = self.janela.Read()

    def Iniciar(self):
        while True:
            #Continua extraindo dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values["nome"]
            idade = self.values["idade"]
            aceita_gmail = self.values["gmail"]
            aceita_hotmail = self.values["hotmail"]
            aceita_yahoo = self.values["yahoo"]
            aceita_outlook = self.values["outlook"]
            aceita_cartao = self.values["aceitaCartao"]
            naoaceita_cartao = self.values["naoAceitaCartao"]
            velocidade_slider = self.values["sliderVelocidade"]
            print(f"Nome: {nome}")
            print(f"Idade: {idade}")
            print(f"Gmail: {aceita_gmail}")
            print(f"Hotmail: {aceita_hotmail}")
            print(f"Yahoo: {aceita_yahoo}")
            print(f"Outlook: {aceita_outlook}")
            print(f"Aceita cartao: {aceita_cartao}")
            print(f"Não aceita cartao: {naoaceita_cartao}")
            print(f"Velocidade Script: {velocidade_slider}")



tela = TelaPython()
tela.Iniciar()