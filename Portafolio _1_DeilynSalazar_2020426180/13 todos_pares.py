" Portafolio #1  |  Deilyn Salazar 2020426180 "

# 13 SI TODOS SON PARES

#E: un número
#S: si todos son pares
#R: solo enteros

def todos_pares(num):
     if isinstance(num, int):
          if num < 0 :
               return todos_pares(num*-1) #para manejar solo positivos
          else:
               return todos_pares_aux(num)
     else:
          return -1 #error en la entrada

#función aux
     
def todos_pares_aux(num):
     if num == 0 :
          return True
     else:
          if (num%10)%2 == 0 :
               return todos_pares_aux(num//10)
          else:
               return False
