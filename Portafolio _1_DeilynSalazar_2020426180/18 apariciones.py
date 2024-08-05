" Portafolio 1 || Deilyn Salazar Murillo 2020426180 "

#18 APARICIONES

#E:
#S:
#R:

def aparecer(num, aparicion):
     if isinstance(num, int) and isinstance(aparicion, int) and aparicion < 10 and aparicion > 0 :
          if num < 0 :
               return aparecer(num*-1, aparicion)
          else:
               if num == 0 :
                    return 0
               elif num%10 == aparicion :
                    return 1 + aparecer(num//10, aparicion)
               else:
                    return aparecer(num//10, aparicion)
     else:
          return -1 #mensaje de errro
