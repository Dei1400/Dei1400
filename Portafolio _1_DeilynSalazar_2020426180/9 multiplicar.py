" Portafolio  |  Deilyn Salazar 2020426180 "

#9 Multiplicación

#E: Dos número
#S: multiplicarlos entres si
#R: números enteros postivos, no usar *

def multiplicar(n,m):
     if isinstance(n, int) and isinstance(m, int) and n >= 0 and m >=0 :
          if m == 0 : #caso base
               return 0
          else :
               return n + multiplicar(n, m-1) #sumar hasta que m sea 0
     else:
          return -1 #mensaje de error en la entrada
