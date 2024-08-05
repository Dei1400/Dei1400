" Portafolio #1  |  Deilyn Salazar 2020426180 "

#11 Número Palindromo

#E: Un número
#S: si es o no palindromo; cuando un número es el mismo al invertirlo
#R:

def palindromo(num):
     if isinstance(num, int) and num > 0 :
          if num == invertir(num) :
               print(num,"=",invertir(num))
               return True
          else:
               print(num,"!=",invertir(num))
               return False
     else:
          return -1 #Error de entrada

#12 invertir
     
#E: un número
#S: invertido
#R: solo enteros

def invertir(num):
     if isinstance(num, int):
          return invertir_aux(num, largo(num)-1)
     else:
          return -1 #Error en la entrada
     
#función auxiliar
     
def invertir_aux(num, largo):
     if num == 0 :
          return 0
     else:
          num2 = (num%10)*(10**largo)
          return num2 + invertir_aux(num//10, largo-1)

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
