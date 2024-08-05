" Portafolio  3  |  Dielyn Salazar Murillo 2020426180 "

#2_Problema: Esta función recibe dos listas. Se
#debe sumar los dos elementos de la misma posición, en caso que una lista sea de largo menor,
#se mantienen los elementos extra de esa lista, el resultado debe ser invertido.

#E: Dos lista
#S: sumar las lista conservar los restante e inverti el resultado
#R: dos elementos tipo lista que no esten vavios y posean solo elementos numericos

def sumaInvertida(lista1, lista2):
     if verificarLista(lista1) == True and verificarLista(lista2) ==  True :
          largo1 = largoL(lista1)
          largo2 = largoL(lista2)
          pos = 0
          res = []
          if largo1 == largo2 :
               while pos != largo1 :
                    res += [lista1[pos]+lista2[pos]]
                    pos += 1
               return invertir(res)
          elif largo1 > largo2 :
               while pos != largo2 :
                    res += [lista1[pos]+lista2[pos]]
                    pos += 1
               res += lista1[pos:]
               return invertir(res)
          else:
               while pos != largo1 :
                    res += [lista1[pos]+lista2[pos]]
                    pos += 1
               res += lista2[pos:]
               return invertir(res)
     else:
          print("No cumple con las restriciones. Error en la entrada")
          return False
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
#E: una lista S: invertida R: no tiene
def invertir(lista):
     res = []
     while lista != [] :
          res+= [lista[-1]]
          lista = lista[:-1]
     return res
