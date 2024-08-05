" Portafolio 1  |  Deilyn Salazar Murillo 2020426180 "

# 16 Convierte un número

#E: Un número
#S: multiplicar cada digito con su posición
#R: entero

def convierteNumero(num):
     if isinstance(num, int):
          if num >= 0 :
               return convierteAux(num, largo(num)-1, 0)
          else:
               return -1 * convierteAux((num*-1),largo(num)-1, 0)
     else:
          return -1 #mensaje de error en la entrada
def convierteAux(num, pos, pot):
     print(num, pos, pot, (num%10)*pos*10**pot)
     if num == 0 :
          return 0
     else:
          return (num%10)*pos*10**pot + convierteAux(num//10, pos-1, pot+1)

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
