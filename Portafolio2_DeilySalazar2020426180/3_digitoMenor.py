" Portafolio 2  | Deilyn Salazar Murillo 2020426180 "

#3.Problema: Construir una función que reciba un
#número entero y retorne el dígito menor.

#E: un número
#S: el digito menor
#R: solo números enteros

def digMenor(num):
     if isinstance(num, int):
          if num < 0 :
               return digMenor(num*-1)
          else:
               return digMenorAux(num//10,num%10)
     else:
          return -1 #error en la entrada
def digMenorAux(num, menor):
     if num == 0 :
          return menor
     else:
          if num%10 < menor :
               return digMenorAux(num//10, num%10)
          else:
               return digMenorAux(num//10, menor)
