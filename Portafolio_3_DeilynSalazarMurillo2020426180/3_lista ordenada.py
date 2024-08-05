#3_Problema: Escriba una función recursiva lista_ordenada (lista, ordenamiento), que reciba una lista y las
#letras ‘a’ o ‘d’ y devuelva True si la lista esta ordenada ascendentemente si el parámetro
#ordenamiento fue ‘a’, o False en caso contrario. Si el parámetro ordenamiento fue ‘d’ debe
#devolver True si la lista está ordenada de forma descendente, en caso contrario False.
#con cualquiera de las dos opcion debe también retornar una neuva lista ordenada seguún la opcion.


#E: una lista y un string
#S: si esta ordenado segun las opciones, y retornar la lista ordenada
#R: la lsita no debe ser vacia y solo debe tenr elementos numericos

def lista_ordenada(lista, ordenamiento):
     if verificarLista(lista) == True :
          if ordenamiento == "a" or ordenamiento == "A" :
               if verificarAscend(lista) == True :
                    return True, lista
               else:
                    for recorrido in range(1, largoL(lista)):
                         for pos in range(largoL(lista)-recorrido):
                              if lista[pos] > lista[pos+1] :
                                   tem = lista[pos]
                                   lista[pos] = lista[pos+1]
                                   lista[pos+1] = tem
                    return False, lista

          elif ordenamiento == "d" or ordenamiento == "D" :
               if verificarDescend(lista) == True :
                    return True, lista
               else:
                    pos = 0
                    for recorrido in range(1, largoL(lista)):
                         for pos in range(largoL(lista)-recorrido):
                              if lista[pos] < lista[pos+1] :
                                   tem = lista[pos]
                                   lista[pos] = lista[pos+1]
                                   lista[pos+1] = tem
                    return False, lista
          else:
               print("Error, ese ordenamiento no existe")
               return False
     else:
          print("Error en la entrada")
          return False

#E: una lista
#S: si esta ordenada de menor a mayor
#R:no tiene
def verificarAscend(lista):
     largo = largoL(lista)-1
     while largo != 0 :
          if lista[largo] > lista[largo-1] :
               largo -= 1
          else:
               return False
     return True
#E: una lista
#S: si esta ordenada de  mayor a menos
#R:no tiene
def verificarDescend(lista):
     largo = largoL(lista)-1
     while largo != 0 :
          if lista[largo] < lista[largo-1] :
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
