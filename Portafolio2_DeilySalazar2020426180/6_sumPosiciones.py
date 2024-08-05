"  Portafolio #2  |  Deilyn Salazar 2020426180  "

#Problema: Construir una función que reciba dos
#listas y retorne una lista con los números posicionales sumados. Las listas pueden
#ser de longitudes diferentes y contener valores heterogéneos

#E: dos listas
#S: la suma de los números en las posiciones
#r: las las eentradas deben ser list y no ser vacias, los valores de la lista deben ser solo numericos

def sumPosiciones(lista1, lista2) :
     if isinstance(lista1, list) and lista1 != [] and isinstance(lista2, list) and lista2 != [] and verificarValoresNumericos(lista1)== True and verificarValoresNumericos(lista2) == True :
          return sumPosicionesAux(lista1, lista2, [])
     else:
          return -1 #error en la entrada
#E: tres listas
#S: la suma de las posiciones
#R:
def sumPosicionesAux(lista1, lista2, res):
     if lista1 == [] and lista2 == [] :
          return res
     elif lista1 == [] :
          return sumPosicionesAux(lista1, [], res+lista2)
     elif lista2 == [] :
          return sumPosicionesAux([], lista2, res+lista1)
     else:
          return sumPosicionesAux(lista1[1:], lista2[1:], res+[lista1[0]+lista2[0]])
#e: una lista
#S: si tiene o no solamente valores numericos
#R: en la netrada solo debe ser una lista y no puede estra vacia
def verificarValoresNumericos(lista):
     if isinstance(lista, list) and lista != [] :
          return verificarVNAux(lista)
     else:
          return -1 #error en la entrada
def verificarVNAux(lista) :
     if lista == [] :
          return True
     else:
          if isinstance(lista[0], int) or isinstance(lista[0], float) :
               return verificarVNAux(lista[1:])
          else:
               return False
