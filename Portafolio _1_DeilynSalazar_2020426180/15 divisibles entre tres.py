" Portafolio #1  |  Deilyn Salazar 2020426180 "

#15 DIVISIBLES ENTRE 3

#E:
#S:
#R:

def div3(num):
     if isinstance(num, int) and num > 0 :
          return div3_aux(num, 0)
     else:
          return -1 #error en la entrada
#función auxiliar

def div3_aux(num, pot):
     if num == 0 :
          return 0
     else:
          if (num%10) > 0  and (num%10)%3 == 0 :
               return (num%10)*10**pot + div3_aux(num//10, pot+1)
          else:
               return div3_aux(num//10, pot)
