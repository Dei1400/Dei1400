" Portafolio 3  |  Deilyn Salazar Murillo 2020426180 "

#CUENTAS PARES
#E: un numero
#S: cuenta los dígitos pares
#R: un número entero
def cuentaPares(num):
     if isinstance(num, int):
          if num < 0 :
               num *= -1
          res = 0
          while num > 0 :
               if (num%10)%2 == 0 :
                    res += 1
                    num = num//10
               else:
                    num = num//10
          return res
     else:
          return -1
#CUENTA IMPARES
#E: un numero
#S: cuenta los dígitos impares
#R: un número entero
def cuentaImpares(num):
     if isinstance(num, int):
          if num < 0 :
               num *= -1
          res = 0
          while num > 0 :
               if (num%10)%2 != 0 :
                    res += 1
                    num = num//10
               else:
                    num = num//10
          return res
     else:
          return -1
