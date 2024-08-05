" Portafolio #1  |  Deilyn Salazar 2020426180 "

#14 ORDENAR DESCENDENTEMENTE

#E: un número
#S: ordenarlo descendente
#R: solo enteros positivos

def ordenar_descendente(num):
     if isinstance(num ,int) and num > 0 :
          if num == 0 :
               return 0
          else:
               return ordenar_d_aux(num, num, 0, 0)
     else:
          return -1 #error en la entrada

#función aux

def ordenar_d_aux(num1, num2, dig, pot):
     if dig > 9 :
          return 0
     else:
          if num1 == 0 :
               return ordenar_d_aux(num2, num2, dig+1, pot)
          elif num1%10 == dig :
               return (dig*10**pot)+ordenar_d_aux(num1//10,num2, dig, pot+1)
          else:
               return ordenar_d_aux(num1//10, num2, dig,pot)
