" Portafolio 2  | Deilyn Salazar 2020426180  "



#Problema: Realizar una función que tome
#un número y sume los dígitos
#impares del número

#E: un número
#s: sumas sus digitos impares
#R: solo números enteros positivos

def sumImpares(num):
     if isinstance(num, int) and num > 0 :
          return sumImparesAux(num, 0)
     else:
          return -1 #error en la entrada
     
#E: un número
#s: sumas sus digitos impares
#R: no tiene
     
def sumImparesAux(num, suma):
     if num == 0 :
          return suma
     else:
          if (num%10)%2 == 0 :
               return sumImparesAux(num//10, suma)
          else:
               return sumImparesAux(num//10, suma+(num%10))
