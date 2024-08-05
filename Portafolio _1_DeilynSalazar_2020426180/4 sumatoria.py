" Portafolio #1  |  Deilyn Salazar 2020426180 "

#4  SUMATORIA

#E: Un número
#S: su sumatoria
#R: solo enteros positivos

def sumatoria(num):
     if isinstance(num, int) and num > 0 : #restriccion para enteros positivos
          if num == 0 :
               return 0
          elif num == 1 :
               return 1
          else:
               return num + sumatoria(num-1)
     else:
          return -1 #mensaje de error en la entrada
