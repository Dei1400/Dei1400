" Portafolio #2  |  Deilyn Salazar Murillo 2020426180 "


#Problema: Construir una función que forme un
#número a partir de otro, considerando sólo los dígitos impares del número de
#entrada.

#E:Un número
#S: nuevo número considerando los impares del númeor en la entrada
#R: solo número entero en la entrada
#(cero es par)

def nuevoNumImpares(num) :
     if isinstance(num, int) :
          if num == 0 :
               return 0
          elif num < 0 :
               return imparesAuxNegativos(num*-1, 0, 0)
          else :
               return imparesAuxPositivos(num, 0, 0)
     else:
          return "Error en la entrada"
#E:tres números
#S: nuevo número considerando los impares del número en la entrada (positivos)
#R: no tiene
def imparesAuxPositivos(num, res, pot):
     if num == 0 :
          return res
     else:
          if (num%10)%2 == 0 :
               return imparesAuxPositivos(num//10, res, pot)
          else:
               return imparesAuxPositivos(num//10, res+((num%10)*10**pot), pot+1)
#E:tres número
#S: nuevo número considerando los impares del númeor en la entrada (negativos)
#R: no tiene
def imparesAuxNegativos(num, res, pot):
     if res < 0 :
          return res
     elif num == 0 :
          return imparesAuxNegativos(num, res*-1, pot)
     else:
          if (num%10)%2 == 0 :
               return imparesAuxNegativos(num//10, res, pot)
          else:
               return imparesAuxNegativos(num//10, res+((num%10)*10**pot), pot+1)
