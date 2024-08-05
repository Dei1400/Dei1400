"  Portafolio #2  |  Deilyn Salazar 2020426180  "

#Problema: Crear una función que reciba una lista
#con elementos numero en la entrada y retorne una nuevo
#con las palabras par e impar seguún el elemento. (par si el elemento es par)(impar si el elemnto es impar)

#E: una lista
#S: una nueva lista con las palabras apr e impar segun sea ele elemnto
#R: la lista no puede ser vacia, y solo tener elementos numericos

def listaParEImpar(lista):
     if isinstance(lista, list) and lista != [] and verificarLista(lista) == True :
          return listaParEImparAux(lista, [], largoLista(lista), 0)
     else:
          return -1 #error en la entrada
def listaParEImparAux(lista, nueva, largo, pos):
     if largo == 0 :
          return nueva
     else:
          if (lista[pos])%2 == 0 :
               return listaParEImparAux(lista, nueva+["par"], largo-1, pos+1)
          else:
               return listaParEImparAux(lista, nueva+["Impar"], largo-1, pos+1)
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
          if (isinstance(lista[pos], int) or isinstance(lista[pos], float)) and lista[pos] > 0 :
               return verificarListaAux(lista, pos+1)
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
