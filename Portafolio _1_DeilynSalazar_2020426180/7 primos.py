" Portafolio #1  |  Deilyn Salazar 2020426180 "

# 7 PRIMOS

#E: un número
#S: si es primo o no
#R: solo enteros 

def primos(num):
     if isinstance(num, int):
          if num < 0:
               return False #los número negativos no son primos
          else:
               return primos_aux(num, 2) #función auxiliar
     else:
          return -1 #mensaje de error en la entrada

#función auxiliar
#E: un número
#S: si es primo o no
#R: no tiene

def primos_aux(num, div):
     if num % div == 0  and num != 2 : #si es divisible, y no es 2, es falso
          return False
     elif div > num/2 : #si llega a la mitad termina
          return True
     else:
          return primos_aux(num, div+1) #se le suma al divisor
