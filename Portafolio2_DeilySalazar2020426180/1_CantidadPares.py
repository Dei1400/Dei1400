" Portafolio 2  | Deilyn Salazar Murillo 2020426180 "

#1.Problema: dado un número entero indique la
#cantidad de dígitos pares que posee.

#E: Un número
#S: La cantidad de pares que posee
#R: solo enteros

def cantidadPares(num):
     if isinstance(num, int):
          if num == 0 :
               return 1 #TOMANDO A CERO COMO PAR
          elif num < 0 :
               return cantidadPares(num*-1) #convertir el númerp negativo a positivo
          else:
               return cantidadParesAux(num, 0, 0)
     else:
          return -1 #error en la entrada
def cantidadParesAux(num, pot, res):
     if num == 0: #ESTE CERO ES DE CUANDO EL NUMERO YA FUE REDUCIDO AL MAXIMO
          return res
     else:
          if (num%10)%2 == 0:
               return cantidadParesAux(num//10, pot+1,res+1)
          else:
               return cantidadParesAux(num//10, pot+1,res)
