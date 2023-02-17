import traceback


def main():
    seguir_jugando = True
    nombre = input("¿Cómo te llamas? ").lower().capitalize()
    menu(nombre, seguir_jugando)

# Método que imprime el menú por la terminal.
def menu(nombre: str, seguir_jugando: bool):
    try:
        while (seguir_jugando):
            print('\033[95m' + "\n------------------------" + '\033[0m')
            print('\033[95m' + "Hola " + nombre + "!!" + '\033[0m')
            print('\033[95m' + "¿ Qué quieres hacer ? 🤔" + '\033[0m')
            print('\033[95m' + "1. Jugar 🎮\n2. Añadir una palabra 🤓\n3. Salir 👋" + '\033[0m')
            print('\033[95m' + "------------------------")
            opcion = (input('\033[95m' + " + Introduce una opción: " + '\033[0m'))
            #print('\n')
            if opcion == '1':
                jugar()
            elif opcion == '2':
                introducirPalabra()
            elif opcion == '3':
                exit()
            else:
                print('\033[90m' + "\n***Escoge una opción válida***" + '\033[0m')
                menu(nombre, seguir_jugando)

            respuesta = ""
            while((respuesta.lower() != 'n') and (respuesta.lower() != 'no') and (respuesta.lower() != 's') and (respuesta.lower() != 'si')):
                respuesta = input('\033[95m' + "¿Quiéres seguir jugando? (s/n)   " + '\033[0m')
                if (respuesta.lower() == 'n') or (respuesta.lower() == 'no'):
                    seguir_jugando = False
                elif(respuesta.lower() == 's') or (respuesta.lower() == 'si'):
                    seguir_jugando = True

    except Exception:
        print('\033[90m' + "\n***Escoge una opción válida***" + '\033[0m')
        traceback()
        menu(nombre, seguir_jugando)


# Método para jugar al ahorcado.
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
    #print(palabra_escogida)

    lista_letras_utilizadas = []
    acertar_palabra = False
    fallos = 0

    # 2. Definimos la palabra del usuario con barra bajas.
    palabra_usuario = ""

    for x in palabra_escogida:
        palabra_usuario += "_"
    print("\nLa palabra es: " + '\033[96m' + palabra_usuario + '\033[0m')

    while (acertar_palabra == False):

        letra_repetida = True
        while (letra_repetida):
            # Pedir al usuario las letras para adivinar la palabra escondida.
            letra = input("\n- Dime una letra: ").lower()
            #print(letra)
            # Comprobamos si la letra no se ha utilizado antes.
            if (letra in lista_letras_utilizadas):
                print('\033[36m' + "Esta letra ya la has utilizado." + '\033[0m')
            elif (comprobarCaracteresErroneos(letra)):
                letra_repetida = True
            elif len(letra) > 1 or len(letra) < 1:
                    if len(letra) > 1:
                        print('\033[33m' + 'Te he pedido una letra, no la biblia. 🤨' + '\033[0m')
                    else:
                        print('\033[33m' + 'Te he pedido una letra, no el vacío. 😗' + '\033[0m')    
                    letra_repetida = True
            else:
                lista_letras_utilizadas.append(letra)
                letra_repetida = False

        # Si he acertado la letra
        if (letra in palabra_escogida):

            # Imprimimos la palabra escondida con las letras acertadas.
            palabra_nexo = ""
            for x in range(len(palabra_escogida)):
                if (letra == palabra_escogida[x]):
                    palabra_nexo += letra
                else:
                    palabra_nexo += palabra_usuario[x]

            palabra_usuario = palabra_nexo

            # Comprobamos si ha acertado la palabra.
            if (palabra_escogida == palabra_usuario):
                acertar_palabra = True
                print('\n' + '\033[92m' + "HAS ACERTADO LA PALABRA !!" + '\033[0m')
            # Si no es el caso, aumentamos en una unidad los fallos del usuario.
        else:
            fallos += 1
            if (fallos < 5):
                # print("Tienes {} fallos. (El máximo son 5).".format(fallos))
                print('\033[94m' + ahorcado[fallos] + '\033[0m')
            if (fallos == 5):
                print('\033[95m' + "Has perdido 💀" + '\033[0m')
                print("La palabra era --> " + '\033[95m' + palabra_escogida + '\033[0m')
                break
        print( '\033[91m' + "Tienes {} fallos. (El máximo son 5).".format(fallos) + '\033[0m')
        #print('Has utilizado: ' + lista_letras_utilizadas)
        print("La palabra es: " + '\033[96m' + palabra_usuario + '\033[0m')


# Método para introducir una palabra.
def introducirPalabra():
    escribiendo = True
    while (escribiendo):
        escribiendo = escribir()
    leer()


# Método que comprueba si la palabra introducida por el usuario contiene algún caracter erróneo.
def comprobarCaracteresErroneos(palabra: str):
    file_error = open('CaracteresIncorrectos.txt', 'r')
    caracteres_erroneos = file_error.read()
    caracteres_erroneos_palabra = ""

    for x in palabra:
        for y in caracteres_erroneos:
            if (x == y):
                caracteres_erroneos_palabra += y

    if (len(caracteres_erroneos_palabra) > 0):
        print("**La palabra contiene algún caracter inválido ({})".format(caracteres_erroneos_palabra))
        return True
    else:
        return False


# Método para que el usuario introduzca una palabra
def escribir():
    # 1. Pedir palabra al usuario.
    palabra = input("Dime una palabra: ")
    # 1.1 Pasamos la palabra a minúscula y le quitamos los espacios laterales.
    palabra = palabra.lower().strip()

    # 2. Comprobamos si la palabra del usuario no está ya en la lista
    file_r = open('Palabras.txt', 'r')
    lista_palabras = file_r.read().split(',')

    for y in lista_palabras:
        if (palabra == y.lower()):
            return False

    # 3. Comprobamos si la palabra del usuario tiene un caracter no válido.
    if (not comprobarCaracteresErroneos(palabra)):
        palabra = palabra.capitalize().replace(' ', '')
        # 4. Abrimos el archivo
        file_w = open('Palabras.txt', 'a')
        # 4.1 Añadimos a la lista de palabras la introducida por el usuario.
        file_w.write(',' + palabra)
        # 4.2 Cerramos el archivo.
        file_w.close()
        # 4.3 Dejamos de escribir.
        return False

    # Si no ha entrado en el if anterior, es que hay algún carácter incorrecto.
    # Por tanto, volvemos a preguuntar por una palabra.
    return True


# Método que devuelve la lista de palabras para adivinar.
def leer():
    file_r = open('Palabras.txt', 'r')
    lista_palabras = file_r.read().split(',')
    file_r.close()
    return lista_palabras


main()
