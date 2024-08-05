" Portafolio #1  | Deilyn Salazar 2020426180 "

#5 SUMAR DIGITOS

#E: Un número
#S: sumar sus digitos
#R: solo enteros positivos

def sumar_digitos(num):
     if isinstance(num, int) and num >= 0:
          if num == 0:
               return 0
          else:
               return num%10 + sumar_digitos(num//10) #se corta el ultimo número
                    #se sacar el ultimo número
