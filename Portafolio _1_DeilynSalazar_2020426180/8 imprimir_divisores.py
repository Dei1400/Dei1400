" Portafolio #1  |  Deilyn Salazar 2020426180 "

#8 IMPRIMIR DIVISORES DESCENDENTE

#E: Un número
#S: imprimir sus divisores
#R: solo números enteros, menores a 1950

def div_imprimir(num):
     if isinstance(num, int):
          if num > 1950 :
               return -1 #después de ese número hace recuersión maxima
          else:
               divisor = str(num)
               return divisor + "," + div_imprimir_aux(num, int(num/2)) # agrega el número (todo número se puede dividir por le mismo)
     else:                                                              #luego solo mando la mitad del número
          return -1 #mensaje de error
def div_imprimir_aux(num, div):
     if div == 0: #caso base
          return ""
     else:
          if num%div == 0 : #si el modulo del divisor es 0, si es un divisor de ese número
               divisor = str(div) #hacerlo str
               return divisor + "," + div_imprimir_aux(num, div-1)#se le resta uno al divisor para pobar otro número
          else:
               return div_imprimir_aux(num, div-1)#se le resta uno al divisor para pobar otro número
