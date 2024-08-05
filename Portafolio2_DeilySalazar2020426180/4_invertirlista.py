" Portafolio 2  |  Deilyn Salazar 2020426180 "

#4.  Problema: Construir una función que reciba una lista y la retorne invertida.

#E: una lista
#S: la lista invertida
#R: solo listas en la entrada

def invertirLista(lista):
     if isinstance(lista, list) and lista != [] :
          return invertirListaAux(lista, largoLista(lista), largoLista(lista)-1,[])
     else:
          return -1 #error en la entrada
def invertirListaAux(lista, largo, pos, invertida):
     if largoLista(invertida) == largo :
          return invertida
     else:
          return invertirListaAux(lista, largo, pos-1, invertida+ [lista[pos]])
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


