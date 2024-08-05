"  Portafolio 3  |  Deilyn Salazar M 2020426180  "

#Problema: Separa los número pares e impares de una matriz en listas disferentes

##E: Una matriz
#S: separar los numeros pares e impares
#R: validar matriz, que sea solo númerica

def separarPeI(matriz) :
     if validarMatriz(matriz) == True and matrizNumerica(matriz) == True :
          filas = largoL(matriz)
          f = 0
          colum = largoL(matriz[0])
          c = 0
          p = []
          i = []
          while f != filas :
               while c != colum :
                    if matriz[f][c]%2 == 0 :
                         p += [matriz[f][c]]
                         c += 1
                    else:
                         i += [matriz[f][c]]
                         c += 1
               c = 0
               f += 1
          return "Pares: ", eliminarRepetidos(p), " Impares: ", eliminarRepetidos(i)
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
