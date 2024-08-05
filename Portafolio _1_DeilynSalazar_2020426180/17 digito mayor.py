" Portafolio 1  |  Deilyn Salazar Murillo 2020426180 "

# 17 DIGITO MAYOR

#E: Un número
#S: el digito mayor
#R: solo numeor sneteros positivos

def digitoMayor(num):
     if isinstance(num, int) and num > 0 :
          mayor = num%10
          if mayor < digitoMayor(num//10):
               return digitoMayor(num//10)
          else:
               return mayor
     else:
          return -1
