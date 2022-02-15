def seq_ping():
    print("Ok")

#EXERCISE 1
def valid_filename(FOLDER):
    exit = False
    while not exit:
        filename = input("DNA file:")
        try:
            f= open(FOLDER + filename + ".txt","r")
            exit = True
            return filename
        except FileNotFoundError:
            print("This file has not been found")

#EXERCISE 2
#Ejercicio 2: seq_read_fasta()
#Implemente la función seq_read_fasta(nombre de archivo) .
# Debería abrir un archivo, en formato FASTA, y devolver un String con la secuencia de ADN .
# Se elimina la cabeza, así como los caracteres '\n'. Esta función debe escribirse en el archivo Seq0.py
#Nombre de archivo : P0/Ex2.py
#Descripción : escriba un programa en python para abrir el archivo U5.txt y escribir en la consola las primeras
# 20 bases de la secuencia
def seq_read_fasta(filename,FOLDER):
    seq = open(FOLDER + filename + ".txt","r").read()
    new_seq = seq.find("\n")
    seq = seq[new_seq:].replace("\n","")
    return seq

#EXERCISE 3
#Ejercicio 3: seq_len()
#Implemente la función seq_len(seq) , que calcula el número total de bases en la secuencia.
#Debe estar escrito en el archivo Seq0.py
#Nombre de archivo : P0/Ex3.py
#Descripción : escriba un programa en Python
#para calcular la longitud total de los 5 genes: U5, ADA, FRAT1, FXN y U5.
#El programa debe llamar a la función seq_len()
#Consideraciones :
#Crea una lista con los nombres de los Genes
#El nombre del archivo se puede obtener agregando la cadena ".txt" al nombre del gen
#Use un ciclo for para iterar sobre los 5 genes y calcular sus longitudes

def seq_len(seq):
    list_genes = []
    for i in seq:
        list_genes.append(len(seq_read_fasta(i)))
    return list_genes

#EXERCISE 4
#Ejercicio 4: seq_count_base()
#Implemente la función seq_count_base(seq, base) , que calcula el número de veces
# que aparece la base dada en la secuencia. Debe estar escrito en el archivo Seq0.py
#Nombre de archivo : P0/Ex4.py
#Descripción : escriba un programa de Python para calcular el número de cada
# base ubicada en cada uno de los cinco genes
#Consideraciones :
#Crea una lista con las cuatro bases .
#Para cada gen, iterar sobre las bases, imprimiendo su número
def seq_count_base(seq):
    #seq = open("./sequences/" + seq + ".txt", "r").read()
    #seq = seq[seq.find("\n"):].replace("\n", "")
    data_list = []
    for i in seq:
        data_list.append(seq_read_fasta(i))
    return seq

#Ejercicio 5: seq_count()
#Implemente la función seq_count(seq) , que calcula el número de veces
# que aparecen todas las bases en la secuencia. Devuelve un diccionario con
# toda la información.
# Las claves del diccionario son las bases: 'A', 'T', 'C' y 'G'.
# Debe estar escrito en el archivo Seq0.py
#Nombre de archivo : P0/Ex5.py
#Descripción : escriba un programa en Python para calcular el
# número de cada una de las bases ubicadas en cada uno de los cinco genes.
# Es similar al ejercicio 4, pero lo que se imprime en la consola es el diccionario devuelto por la
# función seq_count()

















