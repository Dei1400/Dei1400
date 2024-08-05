" Portafolio #1  |  Deilyn Salazar 2020426180 "

# 6 LARGO DE UN NÚMERO

#E: Un número
#S: Cuantos digitos posee
#R: solo enteros

def largo(num):
     if isinstance(num, int):
          if num < 0 : #para manejar el número en positivo
               return largo(num*-1)
          elif num < 10  and num >= 0 : #caso base
               return 1
          else:
               return 1+ largo(num//10) #se llama a la funcion cortando el ultimo digito del número
     else:
          return -1 #mensaje de error en la entrada
