" Portafolio 3  |  Deilyn Salazar Murillo 2020426180 "

#Esta función debe sustituir cualquier elemento que
#aparezca en la sublista por el elemento en la lista.

#E: Dos listas y un elemento
#S: sustituir los elemento de sublista
#en la lista por el elemento ingresado
#R: los elementos listas no deben ser vacios

def sustituir(sublista, elemento, lista):
     if isinstance(sublista, list) and isinstance(lista, list) and sublista != [] and lista != []:
          
          pos1 = 0
          pos2 = 0

          while lista[pos1:] != []:
               while sublista[pos2:] != []:
                    if lista[pos1] == sublista[pos2]:
                         lista[pos1] = elemento
                         pos2 += 1
                    else:
                         pos2 += 1
               pos1 += 1
               pos2 = 0
          return lista
