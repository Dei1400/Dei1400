" Portafolio 3  |  Deilyn Salazar Murillo 2020426180 "

#Si la lista1 se encuentra dentro de la lista2 devuelve
#los elementos posteriores a la primera aparición de la
#lista1, en caso contrario devuelve False

def encuentrarEnLista(lista1, lista2):
     if isinstance(lista1, list) and isinstance(lista2, list) and lista1 != [] and lista2 != []:
          if largoL(lista1) > largoL(lista2):
               return False
          else:
               pos1 = 0
               pos2 = 0
               while lista1[pos1:] != [] :
                    if lista2[pos2:] == [] :
                         return False
                    elif lista1[pos1] == lista2[pos2]:
                         pos1 += 1
                         pos2 += 1
                    else:
                         pos1 = 0
                         pos2 += 1
               pos2 = pos2-largoL(lista1)
               return lista2[:pos2]
#E: una lista s: su largo r: no tiene
def largoL(lista):
     largo = 0
     while lista != [] :
          largo += 1
          lista= lista[1:]
     return largo
