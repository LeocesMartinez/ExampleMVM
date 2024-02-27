import re

alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L",
            "M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
         "..", ".---", "-.-", ".-..", "--", "-.", "--.--", "---", ".--.",
         "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",
         "-----", ".----", "..---", "...--", "....-", ".....", "-....",
         "--...", "---..", "----.", " "]

def menu():
    centinela = 0
    while centinela == 0:
        print("Escriba 1 para mostrar el mensaje en clave MORSE")
        print("Escriba 2 para mostrar el mensaje en ALFABETO")
        print("Presione cualquier otra tecla para salir")
        option = input()
        
        if option.upper() == "1":
            print("Escriba su mensaje" + "\n")
            message = input().upper()
            try:
                if not re.match(r'^[a-zA-Z0-9-ñÑ\s]+$', message):
                    raise Exception("\n" + "El mensaje solo debe contener letras y números." + "\n")
                
                print(encriptador(message))
            except Exception as e:
                print("\n" + "El mensaje solo debe contener letras y números." + "\n")
                
        elif option.upper() == "2":
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
        indice = buscadorAlfabeto(letra, alfabeto)
        if indice != -1:
            acumulador += morse[indice] + " "
    return "\nSu mensaje en clave Morse es: " + acumulador + "\n"

def buscadorAlfabeto(letra, alfabeto):
    for i, cadena in enumerate(alfabeto):
        if letra in cadena:
            return i
    return -1

def desencriptador(mensaje):
    acumulador = ""
    try:
        letras = mensaje.split(' ')
        for letra in letras:
            indice = buscadorMorse(letra)
            acumulador += alfabeto[indice]
    except Exception as ex:
        print("Ha ingresado un caracter de forma inválida" + "\n")
    return "\nSu mensaje es: " + acumulador + "\n"

def buscadorMorse(letra):
    for i, morse_code in enumerate(morse):
        if letra == morse_code:
            return i
    return -1

if __name__ == "__main__":
    menu()
