" Portafolio #1  |  Deilyn Salazar 2020426180 "

# 10 FIBONACCI

#E: Un número
#S: su fibonacci
#R: solo enteros positivos

def fibonacci(num):
     if isinstance(num, int) and num > 0 :
          return fibonacci_aux(num) #función auxiliar
     else:
          return -1 #mensaje de error en la entrada
#función auxiliar
#E: Un número
#S: su fibonacci
#R: no tiene
def fibonacci_aux(num):
     if num == 0 :
          return 0  #dos casos base cero y uno
     elif num == 1 :
          return 1
     else:
          return fibonacci_aux(num-1) + fibonacci_aux(num-2)
