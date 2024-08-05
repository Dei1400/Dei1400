" Portafolio 2  | Deilyn Salazar Murillo 2020426180 "

#2. Problema: Construir una función que reciba una
#lista y por cada número genere una sublista de sus divisores, si no es número
#entero reemplaza el elemento por un -1.

#E: una lista de numeros
#S: por cada número una sublista de sus divisores
#R: la lsita solo puede tner elementos numericos

def subDivisores(lista):
     if isinstance(lista, list)and lista != [] and verificarLista(lista) == True:
          return subDivisoresAux(lista,0,[])
     else:
          return -1 #error en la entrada
def subDivisoresAux(lista, pos, res):
     if largoLista(lista) == pos :
          return res
     else:
          if isinstance(lista[pos], int):
               return subDivisoresAux(lista, pos+1,res+[divisores(lista[pos])])
          else:
               return subDivisoresAux(lista, pos+1,res+[-1])
               
#***************************************
#función para saber los divisores
#E: un número
#S: un lista con sus divisores
#R: solo numeros enteros
def divisores(num):
     if isinstance(num, int):
          if num < 0 :
               return divisores(num*-1)
          else:
               return divisoresAux(num, 1, [])
def divisoresAux(num, div, res):
     if div == num :
          return res+[num]
     else:
          if num%div == 0 :
               return divisoresAux(num, div+1, res+[div])
          else:
               return divisoresAux(num, div+1, res)

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
