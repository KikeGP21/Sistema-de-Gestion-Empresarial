import fitz
import mariadb
import sys


def lector():

    global lista_palabras_pdf

    pdf = fitz.open(
        'LEER DOCUMENTO/Autorización de funcionamiento de sala de bingo-ABG.pdf')
    pdf_reader = pdf.load_page(0)
    texto_pdf = pdf_reader.get_text()

    lista_palabras_pdf = texto_pdf.split("\n")

    documento_txt = open('Palabras copy.txt', 'a')
    documento_txt.write()

    for x in lista_palabras_pdf:
        # En el caso del sexo, es una casilla marcada,  # asi que, he hecho un if para comprobar el código ascii.  # Compruebo que el primer cuadrado tenga tic y si no, será el segundo  
        if listaSexo[0] == "\uf0fe": 
            sexo = "masculino"
            documento_txt.write("Sexo --> Masculino" + "\n") 
        else : sexo = "femenino"
        documento_txt.write("Sexo --> Femenino" + "\n")
        documento_txt.write("Correo Electrónico --> " + listaCorreo[2] + "\n")
        documento_txt.write("Teléfono Móvil --> " + listaTelefono[3] + "\n")
        documento_txt.write("Razón Social / Denominación --> " + lista_palabras_pdf[7] + "\n") 
        documento_txt.write("NIF --> " + lista_palabras_pdf[9] + "\n")
        documento_txt.write("Código de Inscripción --> " + lista_palabras_pdf[11] + "\n")
        documento_txt.write("Domicilio --> " + lista_palabras_pdf[16] + " ,tipo de vía --> " + lista_palabras_pdf[14] + "\n")
        documento_txt.write("Entidad de Población --> " + lista_palabras_pdf[26] + "\n")
        documento_txt.write("Municipio --> " + lista_palabras_pdf[28] + "\n")
        documento_txt.write("Provincia --> " + lista_palabras_pdf[30] + "\n")
        documento_txt.write("País --> " + lista_palabras_pdf[32] + "\n")
        documento_txt.write("Código Postal --> " + lista_palabras_pdf[34] + "\n")
        documento_txt.write("Apellidos y Nombre --> " + lista_palabras_pdf[36] + "\n")      
        documento_txt.write("DNI/NIE/NIF --> " + lista_palabras_pdf[40] + "\n")
        documento_txt.write("Actúa en calidad de --> " + lista_palabras_pdf[42] + "\n") 

    # print(lista_palabras_pdf)
    # lista_palabras = pdf.split("\n")
    # print(lista_palabras)
    pdf.close()


lector()
