import webbrowser as wb
import keyboard
import os
import time
from random import randint

def clear():
    os.system("cls")        #Clear console in cmd

def credits():
    print("Developped by M-Malo")         #Display credits

def random_url(url,n):      #build a single url
    result = ""
    for i in range(0,n):
        if randint(0,1) == 0:
            result += str(randint(0,9))
        else:
            result += str(chr(randint(97,122)))
    return url + result

def open_url():
    for j in range(0,NombreDePage):         #build an amount n of url
        time.sleep(0.1)
        wb.open_new_tab(random_url(url,6))

def main():
    #Init
    global url
    global NombreDePage
    stop = False
    keyadded = False

    #Config
    url = "https://prnt.sc/"

    #Moteur
    clear()
    credits()
    NombreDePage = int(input("Combien de page voulez vous ouvrir ?"))
    while stop is False:
        clear()
        if keyadded is False:           #config the key combination to open new screenshots
            keyboard.add_hotkey("ctrl + x", open_url)
            keyadded = True
        reponse = input("CTRL + X pour ouvrir une page\nconfig pour choisir le nombre de page a ouvrir\nexit pour quitter le programme")
        if reponse == "config":
            print(reponse)
            clear()
            NombreDePage = int(input("Combien de page voulez vous ouvrir ???"))
        if reponse == "exit":
            stop = True

if __name__ == "__main__":
    main()