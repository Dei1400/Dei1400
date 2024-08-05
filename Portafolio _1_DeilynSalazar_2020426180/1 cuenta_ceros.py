" Portafolio #1  | Deilyn Salazar 2020426180 "

#1 CUENTA CEROS

#E: Un número
#S: La cantidad de ceros que posee el número
#R: solo permitir números enteros

def cuenta_ceros(num):
     if isinstance(num, int):
          if num < 0 :                     #Multiplicar por menos uno para
               return cuenta_ceros(num*-1) #utilizar el número en positivo
          elif num == 0 :                  
               return 1
          else:
               return cuenta_ceros_aux(num)
     else:
          return -1 #Mensaje de error en la entrada
     
#función auxiliar
#E: Un número
#S: La cantidad de ceros que posee el número
#R: no tiene
def cuenta_ceros_aux(num):
     if num == 0 : #condición de parada (caso base)
          return 0 #no sumo porque no es un cero del número, es el cero de que termino de cortar el número
     else:
          if num%10 == 0 : # sacar el ultimo uno con modulo de 10, y comparlo con cero
               return 1 + cuenta_ceros_aux(num//10) #se deja un uno para sumar, se divide por diez para cortar el ultimo número
          else:
               return cuenta_ceros_aux(num//10)
               #se vuleve a llamar la función pero sin sumar, igual se corta el ultimo número
