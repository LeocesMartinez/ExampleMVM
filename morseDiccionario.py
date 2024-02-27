import re

alfabeto_morse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "Ñ": "--.--", "O": "---", "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--",
    "X": "-..-", "Y": "-.--", "Z": "--.."}
#,
    #"0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    #"5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    #" ": " "


def menu():
    centinela = 0
    while centinela == 0:
        print("Escriba 1 para mostrar el mensaje en clave MORSE")
        print("Escriba 2 para mostrar el mensaje en ALFABETO")
        print("Presione cualquier otra tecla para salir")
        option = input()
        
        if option == "1":
            print("Escriba su mensaje" + "\n")
            message = input().upper()
            try:
                if not re.match(r'^[a-zA-Z0-9-ñÑ\s]+$', message):
                    raise Exception("\n" + "El mensaje solo debe contener letras y números." + "\n")
                
                print(encriptador(message))
            except Exception as e:
                print("\n" + "El mensaje solo debe contener letras y números." + "\n")
                
        elif option == "2":
            print("\n" + "Escriba su mensaje, cada caracter tipo morse separado por un espacio por favor" + "\n")
            message = input()
            try:
                if not re.match(r'^[. -]+$', message):
                    raise Exception("\n" + "El mensaje solo debe contener caracteres tipo Morse válidos." + "\n")
                
                print(desencriptador(message))
            except Exception as e:
                print("\n" + "El mensaje solo debe caracteres Morse válidos." + "\n")
                
        else:
            print("Ha elegido salir, gracias hasta pronto!")
            centinela = 1

def encriptador(mensaje):
    acumulador = ""
    for letra in mensaje:
        if letra in alfabeto_morse:
            acumulador += alfabeto_morse[letra] + " "
    return "\nSu mensaje en clave Morse es: " + acumulador + "\n"

def desencriptador(mensaje):
    acumulador = ""
    try:
        letras = mensaje.split(' ')
        for letra in letras:
            for key, value in alfabeto_morse.items():
                if letra == value:
                    acumulador += key
    except Exception as ex:
        print("Ha ingresado un caracter de forma inválida" + "\n")
    return "\nSu mensaje es: " + acumulador + "\n"

if __name__ == "__main__":
    menu()
