import traceback
def main():
    seguir_jugando = True
    nombre = input("¿Cómo te llamas? ").lower().capitalize()
    menu(nombre, seguir_jugando)

def menu(nombre :str, seguir_jugando : bool):
    try:
        while(seguir_jugando):
            print("\n------------------------")
            print("Hola " + nombre + "!!")
            print("¿ Qué quieres hacer ? 🤔")
            print("1. Jugar 🎮\n2. Añadir una palabra 🤓\n3. Salir 👋")
            print("------------------------")
            opcion = int(input(" + Introduce una opción: "))
            if opcion == 1:
                jugar()
            elif opcion == 2:
                introducirPalabra()
            elif opcion == 3:
                exit()
            else:
                print("\n***Escoge una opción válida***")
                menu(nombre, seguir_jugando)
            
            respuesta = input("¿Quiéres seguir jugando? (s/n)   ")
            if (respuesta == 'n'):
                seguir_jugando = False

    except Exception:
        print("\n***Escoge una opción válida***")
        traceback()
        menu(nombre, seguir_jugando)


def jugar():
    import random

    ahorcado = [
        '''
      +-----+
      |     |
            |
            |
            |
            |
    =========''',
        '''
      +-----+
      |     |
      😁    |
            |
            |
            |
    =========''',
                '''
      +-----+
      |     |
      🙂    |
      👔    |
            |
            |
    =========''',
        '''
      +-----+
      |     |
      😐    |
    🖐👔🖐  |
            |
            |
    =========''',
        '''
      +-----+
      |     |
      😑    |
    🖐👔🖐  |
      🩳    |
            |
    =========''',
        '''
      +-----+
      |     |
      🤕    |
    🖐👔🖐  |
      🩳    |
     👟👟   |
    =========''',
    ]


    # 1.  Leemos las palabras y con la clase random seleccionamos una al azar.
    lista_palabras = leer()
    palabra_escogida = random.choice(lista_palabras).lower()
    print(palabra_escogida)

    lista_letras_utilizadas = []
    acertar_palabra = False
    fallos = 0

    # 2. Definimos la palabra del usuario con barra bajas.
    palabra_usuario = ""

    for x in palabra_escogida:
        palabra_usuario += "_"
    print("La palabra es: " + palabra_usuario)

    while ((acertar_palabra == False)):

        letra_repetida = True
        while(letra_repetida == True):
            # Pedir al usuario las letras para adivinar la palabra escondida.
            letra = input("\n- Dime una letra: ").lower()
            print(letra)
            # Comprobamos si la letra no se ha utilizado antes.
            if(letra in lista_letras_utilizadas):
                print("Esta letra ya la has utilizado.")
            elif(comprobarCaracteresErroneos(letra) == False):
                letra_repetida = True  
            else:
                lista_letras_utilizadas.append(letra)
                letra_repetida = False

        # Si he acertado la letra
        if(letra in palabra_escogida):   

            # Imprimimos la palabra escondida con las letras acertadas.
            palabra_nexo = ""
            for x in range(len(palabra_escogida)):
                if(letra == palabra_escogida[x]):
                    palabra_nexo += letra
                else:
                    palabra_nexo += palabra_usuario[x]

            palabra_usuario = palabra_nexo     

            # Comprobamos si ha acertado la palabra.
            if(palabra_escogida == palabra_usuario):
                acertar_palabra = True
                print("HAS ACERTADO LA PALABRA !!")
            print("La palabra actual es: " + palabra_usuario)
            # Si no es el caso, aumentamos en una unidad los fallos del usuario.    
        else:
            fallos += 1
            print("Tienes {} fallos. (El máximo son 5).".format(fallos))
            print(ahorcado[fallos])
            if(fallos == 5):
                print("Has perdido 💀")
                print("La palabra era -->" + palabra_escogida)
                break
        

def introducirPalabra():
    escribiendo = True
    while (escribiendo):
        escribiendo = escribir()
    leer()


def comprobarCaracteresErroneos(palabra : str):
    file_error = open('CaracteresIncorrectos.txt', 'r')
    caracteres_erroneos = file_error.read()
    caracteres_erroneos_palabra = ""

    for x in palabra:
        for y in caracteres_erroneos:
            if(x == y):
                caracteres_erroneos_palabra += y

    if(len(caracteres_erroneos_palabra) > 0):
        print("**La palabra contiene algún caracter inválido ({})".format(caracteres_erroneos_palabra))
        return False
    else:
        return True


def leer():
    file_r = open('Palabras copy.txt', 'r')
    lista_palabras = file_r.read().split(',')
    print(lista_palabras)
    file_r.close()
    return lista_palabras


def escribir():
    # 1. Pedir palabra al usuario.
    palabra = input("Dime una palabra: ")
    # 1.1 Pasamos la palabra a minúscula y le quitamos los espacios laterales.
    palabra = palabra.lower().strip()
    # 2. Comprobamos si la palabra del usuario tiene un caracter no válido.
    if (comprobarCaracteresErroneos(palabra)):
        palabra = palabra.capitalize().replace(' ', '')
        # 3. Abrimos el archivo
        file_w = open('Palabras copy.txt', 'a')
        # 3.1 Añadimos a la lista de palabras la del usuario.
        file_w.write(',' + palabra)
        # 3.2 Cerramos el archivo.
        file_w.close()  
        return False  
    return True

main()