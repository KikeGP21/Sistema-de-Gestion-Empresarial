import fitz
import mariadb
import sys

def lector():

    global lista_palabras_pdf

    pdf = fitz.open('C:/Users/TECH/OneDrive - CEUAndalucia/Escritorio/py/LEER DOCUMENTO/Autorización de funcionamiento de sala de bingo-ABG.pdf')
    pdf_reader = pdf.
    pdf_page = pdf_reader.pages[0]
    texto_pdf = pdf_page.extract_text()

    lista_palabras_pdf = texto_pdf.split("\n")

    for x in lista_palabras_pdf:
        print(x)

        


    #print(lista_palabras_pdf)
    #lista_palabras = pdf.split("\n")
    #print(lista_palabras)
    pdf.close()

lector()
