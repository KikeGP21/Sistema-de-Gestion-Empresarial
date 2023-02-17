import fitz  # Para instalar: py -version (ej:3.11.1) -m pip install -U pymupdf
import mariadb # Para instalar: py -version (ej:3.11.1) -m pip install -U mariadb


def main():
    pdf = input("¿¿ Quieres que se introduzcan los datos del pdf en el documento de texto ?? (s/n)  ")
    if (pdf.lower() == 'n') or (pdf.lower() == 'no'):
        leer_pdf = False
    elif(pdf.lower() == 's') or (pdf.lower() == 'si'):
        leer_pdf = True
    else:
         leer_pdf = False

    if(leer_pdf):
        lectorPDF()
    

    bbdd = input("¿¿ Quieres que se introduzcan los datos del documento de texto en la bbdd?? (s/n)  ")
    if (bbdd.lower() == 'n') or (bbdd.lower() == 'no'):
        introducir_bbdd = False
    elif(bbdd.lower() == 's') or (bbdd.lower() == 'si'):
        introducir_bbdd = True
    else:
         introducir_bbdd = False

    if(introducir_bbdd):
        mariaDB()

def lectorPDF():

    global lista_palabras_pdf
    global datos_cliente

    # # 1. Abrimos el archivo donde vamos a escribir los datos del cliente.
    # pdf = fitz.open('Autorización de funcionamiento de sala de bingo-ABG.pdf')
    # pdf_reader = pdf.load_page(0) # Primera página
    # texto_pdf = pdf_reader.get_text()

    # lista_palabras_pdf = texto_pdf.split("\n")

    # documento_datos_cliente = open('Datos cliente.txt', 'w', encoding='utf-8')
    
    # # 2. Escribimos los datos del cliente.
    # documento_datos_cliente.write("RAZÓN SOCIAL/DENOMINACIÓN --> " + lista_palabras_pdf[7] + "\n")
    # documento_datos_cliente.write("NIF --> " + lista_palabras_pdf[9] + "\n")
    # documento_datos_cliente.write("CÓDIGO DE INSCRIPCIÓN --> " + lista_palabras_pdf[11] + "\n")
    # documento_datos_cliente.write("DOMICILIO --> " + lista_palabras_pdf[14] + " " + lista_palabras_pdf[16] + "\n")
    # documento_datos_cliente.write("ENTIDAD DE POBLACIÓN --> " + lista_palabras_pdf[26] + "\n")
    # documento_datos_cliente.write("MUNICIPIO --> " + lista_palabras_pdf[28] + "\n")
    # documento_datos_cliente.write("PROVINCIA --> " + lista_palabras_pdf[30] + "\n")
    # documento_datos_cliente.write("PAÍS --> " + lista_palabras_pdf[32] + "\n")
    # documento_datos_cliente.write("CÓDIGO POSTAL --> " + lista_palabras_pdf[34] + "\n")

    # nombre_y_apellidos = lista_palabras_pdf[36].split(" ")
    # documento_datos_cliente.write("NOMBRE --> " + nombre_y_apellidos[1].upper() + "\n")
    # documento_datos_cliente.write("APELLIDO --> " + nombre_y_apellidos[0].upper() + "\n")
    # documento_datos_cliente.write("SEXO --> H\n")
    # documento_datos_cliente.write("DNI --> " + lista_palabras_pdf[40] + "\n")
    # documento_datos_cliente.write("ACTÚA EN CALIDAD DE --> " + lista_palabras_pdf[42] + "\n")
        
    # correo = lista_palabras_pdf[48].split(" ")
    # documento_datos_cliente.write("CORREO ELECTRÓNICO --> " + correo[2] + "\n")
        
    # telefono = lista_palabras_pdf[49].split(" ")
    # documento_datos_cliente.write("Nº TELÉFONO --> " + telefono[3]")

    # pdf.close()
    # print('\n' + '\033[92m' + "Datos insertados en el documento correctamente." + '\033[0m')

    # Guardamos todos los datos en la variable 'datos_cliente' extrayéndolos del documento 'Datos cliente.txt'.
    extraccion_datos = open('Datos cliente.txt', 'r', encoding="utf8")
    datos = extraccion_datos.read().split('\n')
    extraccion_datos.close()

    datos_cliente_mal = datos 
    datos_cliente = []

    for x in range(len(datos_cliente_mal)):
        dato_personal = datos_cliente_mal[x].split(' --> ')
        datos_cliente.append(dato_personal[1])

    for y in datos_cliente:
        print(y)


# Método para insertar los datos del cliente en la bbdd.
def mariaDB():

    try:
        # Inicio de conexión a la bbdd.
        connection = mariadb.connect(
            user="junta-de-andalucia",
            password="junta-de-andalucia",
            host="127.0.0.1",
            port=3306,
            database="junta-de-andalucia"
        )
    except mariadb:
        print('\n' + '\033[41m' + "Ha habido un error al conectarse a la bbdd." + '\033[0m')
        return ""

    try:
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO cliente (RAZON SOCIAL,NIF,CODIGO DE INSCRIPCION,DOMICILIO,POBLACION,MUNICIPIO,PROVINCIA,PAIS,CP,NOMBRE,APELLIDO,SEXO,DNI,CALIDAD,CORREO,TELEFONO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (datos_cliente[0], datos_cliente[1], datos_cliente[2], datos_cliente[3], datos_cliente[4], datos_cliente[5], datos_cliente[6], datos_cliente[7], datos_cliente[8], datos_cliente[9], datos_cliente[10], datos_cliente[11], datos_cliente[12], datos_cliente[13], datos_cliente[14], datos_cliente[15]))

        connection.commit()
        connection.close()
    except mariadb:
        connection.rollback()
        print(print('\n' + '\033[41m' + "Ha habido un error al introducir los datos a la bbdd." + '\033[0m'))



main()
