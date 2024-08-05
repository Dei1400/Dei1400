" Portafolio 3  |  Deilyn Salazar Murillo 2020426180 "

#1_Problema: Esta función recibe una lista que encuentra ordenada y
#se debe retornar una nueva lista con el número insertado en la lista,
#de manera tal que se mantenga el orden creciente de la lista.

#E: Un lista y un número
#S: La lista con el nuevo número, insertado según el orden creciente
#R: En la entrada solo se permiten una lista y luego un número entero o flotante,
#la lista debe ser no vacia y poseersolo elementos numericos

def insertarOrden(lista, num):
     if isinstance(num, int) or isinstance(num, float):
          if verificarLista(lista) == True and verificarOrden(lista) == True :
               largo = largoL(lista)
               res = []
               pos = 0
               while pos != largo :
                    if lista[pos] > num :
                         res += [num]
                         res += lista[pos:]
                         return res
                    else:
                         res += [lista[pos]]
                         pos += 1
               res += [num]
               return res
     else:
          print("No cumple con las restriciones. Error en la entrada")
          return False
#E: una lista
#S: si esta ordenada de menor a mayor
#R:no tiene
def verificarOrden(lista):
     largo = largoL(lista)-1
     while largo != 0 :
          if lista[largo] > lista[largo-1] :
               largo -= 1
          else:
               return False
     return True
#E: una lista
#S: verificar si la lista tiene solo elementos numericos
#R: solo elementos tipo lista, que no este vacia
def verificarLista(lista):
     if isinstance(lista, list) and lista != [] :
          largo = largoL(lista)-1
          while largo != 0 :
               if isinstance(lista[largo], int) or isinstance(lista[largo], float) :
                    largo -= 1
               else:
                    return False
          return True
#E: una lista s: su largo r: no tiene
def largoL(lista):
     largo = 0
     while lista != [] :
          largo += 1
          lista= lista[1:]
     return largo
