"  Portafolio 3  |  Deilyn Salzar 2020426180  "

#Problema: retornar una lista con cada numero primo encontrado en la matriz

#E: una matriz
#S: encontrar los numeros primos en una matriz, retornarlos en una lista sin repetidos
#R:  valir matriz

def encontrarPrimos(matriz):
     if validarMatriz(matriz) == True :
          filas = largoL(matriz)
          f = 0
          colum = largoL(matriz[0])
          c = 0
          res = []
          while f != filas :
               while c != colum :
                    if esPrimo(matriz[f][c]) == True :
                         res += [matriz[f][c]]
                         c += 1
                    else:
                         c += 1
               c = 0
               f += 1
          return eliminarRepetidos(res)
     else:
          return False
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
#E: un número
#S: si es primo
#R: que sea un número entero mayor a 0
def esPrimo(num):
     if num == 2 or num == 3 or num == 5 or num == 7 :
          return True
     elif num%2 == 0 :
          return False
     else:
          d = 2
          while (num//2) > d :
               if num%d == 0 :
                    return False
               else:
                    d += 1
          return True
#E: una lista s: su largo r: no tiene
     
def largoL(lista):
     largo = 0
     while lista != [] :
          largo += 1
          lista = lista[1:]
     return largo
#E: una lista
#S: la lista sin respetidos
#R: no tiene
def eliminarRepetidos(lista):
    if isinstance(lista,list) and lista != [] :
         
        res = [lista[0]]
        lista2 = lista[1:]
        pos = 0
        
        while lista2[pos:] != []:
             
            if existe(res,lista2[pos]) == True:
                pos += 1
            else:
                res += [lista2[pos]] 
                pos += 1
                
        return res

def existe(lista,elemento):
    while lista != []:
        if lista[0] == elemento:
            return True
        else:
            lista = lista[1:]
    return False
     
