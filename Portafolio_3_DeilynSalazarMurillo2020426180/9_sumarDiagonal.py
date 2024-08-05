"  Portafolio 3  |  Deilyn Salazar 2020426180  "

#Problema: Sumar la diagonal de una matriz

#E: una matriz
#s: la suma de su diagonal
#R: validar la matriz, saber si es solo numerica, y que sea cuadrada

def sumarDiagonal(matriz) :
     if validarMatriz(matriz) == True and matrizNumerica(matriz) == True :
          if largoL(matriz) == largoL(matriz[0]) :
               filas = largoL(matriz)
               f = 0
               suma = 0
               while f != filas :
                    suma += matriz[f][f]
                    f += 1
               return suma
          else:
               return False
     else:
          return False #error en la entrada
     
#E: una lista s: su largo r: no tiene
     
def largoL(lista):
     largo = 0
     while lista != [] :
          largo += 1
          lista = lista[1:]
     return largo

#E: una matriz
#S: que si es una matriz valida
#R: elemento tipo lista, no vacio

def validarMatriz(matriz) :
     if isinstance(matriz, list) and matriz != [] :
          filas = largoL(matriz)
          colum = largoL(matriz[0])
          f = 1
          while f != filas :
               if colum == largoL(matriz[f]):
                    f += 1
               else:
                    return False
          return True
     else:
          return False
     
#E: una matriz
#S: si es una amtriz con elemento solo númericos
#R: un elemento tipo lista no vacia
     
def matrizNumerica(matriz) :
     if isinstance(matriz, list) and matriz != [] :
          filas = largoL(matriz)
          f = 0
          while f != filas :
               if listaNumerica(matriz[f]) == True :
                    f += 1
               else:
                    return False
          return True
def listaNumerica(lista):
     largo = largoL(lista)
     l = 0
     while l != largo :
          if isinstance(lista[l], int) or isinstance(lista[l], float) :
               l += 1
          else:
               return False
     return True
