import pyautogui
import time

pyautogui.PAUSE = 0.5

#Passo 1: Abrir o Chrome

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Passo 2: Entrar no site - https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

#Passo 3: Fazer login

pyautogui.click(x=775, y=409)
pyautogui.write("cauacaetanofb@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhasecreta")
pyautogui.press("tab")
pyautogui.press("enter")

#Passo 4: Cadastrar produtos

import pandas

tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    
    pyautogui.click(x=783, y=295)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")    

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)