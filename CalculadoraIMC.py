from datetime import date
from tkinter import *


def calc_imc():
    ano_atual = date.today().year
    nome = str(nome_caixa.get())
    nascimento = int(nasc_caixa.get())
    altura = float(alt_caixa.get())
    peso = float(peso_caixa.get())
    idade = ano_atual - nascimento
    imc = peso / (altura ** 2)
    dados["text"] = f"{nome}, você tem {idade} anos. Seu IMC é {imc:.2f}."

    if imc < 18.5:
        result["text"] = "Você está abaixo do peso."
    elif imc >= 18.5 and imc < 25:
        result["text"] = "Você está no peso ideal."
    elif imc >= 25 and imc < 30:
        result["text"] = "Você está com sobrepeso."
    elif imc <= 30 and imc <= 40:
        result["text"] = "Você está com obesidade."
    else:
        result["text"] = "Você está com obesidade mórbida."


janela = Tk()
janela.title("Calculadora IMC")

texto = Label(janela, text="     Sistema de cálculo de Índice de Massa Corporal (IMC)     ")
texto.grid(padx=10, pady=10)

nome_rotulo = Label(janela, text="Seu nome:")
nome_rotulo.grid()
nome_caixa = Entry(janela)
nome_caixa.grid()
nasc_rotulo = Label(janela, text="Ano de Nascimento:")
nasc_rotulo.grid()
nasc_caixa = Entry(janela)
nasc_caixa.grid()
alt_rotulo = Label(janela, text="Sua altura:")
alt_rotulo.grid()
alt_caixa = Entry(janela)
alt_caixa.grid()
peso_rotulo = Label(janela, text="Seu peso:")
peso_rotulo.grid()
peso_caixa = Entry(janela)
peso_caixa.grid()

calc = Button(janela, text="Calcular IMC", command=calc_imc)
calc.grid(padx=10, pady=10)

dados = Label(janela, text="")
dados.grid(padx=10, pady=10)
result = Label(janela, text="")
result.grid(padx=10, pady=10)

fechar = Button(janela, text="Fechar", command="exit")
fechar.grid(padx=10, pady=10)

janela.mainloop()
