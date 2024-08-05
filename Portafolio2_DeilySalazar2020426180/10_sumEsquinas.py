" Portafolio #2  | Deilyn Salazar Murillo 20204261802 "

#Problema: Realizar una función que
#sume las esquinas de una matriz

#E: una matriz
#S: la suma de sus esquinas
#R: que la matriz solo pose elementos numericos, y sea una matriz con la misma cantidad de columnas y de filas

def sumEsquinas(matriz):
     if validarMatriz(matriz):
          return sumEsquinasAux(matriz)
     else:
          return -1 #error en la entrada
def sumEsquinasAux(matriz):
     largo = largoLista(matriz) #filas de la matriz
     ultimaPos = largoLista(matriz[largo-1]) #ultima posición
     suma = matriz[0][0]+matriz[largo-1][ultimaPos-1]
     return suma
#E: una matriz
#S: si es o no valida (que no sea vacia, que sus elementos seas numericos, que la tenga la misma cantidad de elementos en las filas)
def validarMatriz(matriz):
     if matriz != [] and isinstance(matriz, list): #que sea tipo lista, que no sean vacia
          return validarMatrizAux(matriz, largoLista(matriz), largoLista(matriz[0]), 1)
     else:
          return -1 #error en la entrada
def validarMatrizAux(matriz, fila, columnas, pos):
     if pos == fila :
          return True
     else:
          if largoLista(matriz[pos]) == columnas and verificarLista(matriz[pos]):
               return validarMatrizAux(matriz, fila, columnas, pos+1)
          else:
               return False
#************************************************
#función para saber el largo de una lista
#E: una lista
#S: el largo (numero de elementos que posee)
#R: solo una lista en la entrada
def largoLista(lista):
     if isinstance(lista, list):
          return largoListaAux(lista, 0)
     else:
          return -1
def largoListaAux(lista, largo):
     if lista == [] :
          return largo
     else:
          return largoListaAux(lista[1:], largo+1)
#***********************************************
#funcion que verifica qaue la lista solo tenga números
#E: un lista
#S: true or false, si sus elementos son todos numericos
#R: solo una lista como entrada
def verificarLista(lista):
     if isinstance(lista, list) and lista != [] :
          return verificarListaAux(lista, 0)
     else:
          return -1 #error en la entrada

def verificarListaAux(lista, pos):
     if largoLista(lista) == pos :
          return True
     else:
          if isinstance(lista[pos], int) or isinstance(lista[pos], float) :
               return verificarListaAux(lista, pos+1)
          else:
               return False
