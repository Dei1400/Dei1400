"  Portafolio #2  |  Deilyn Salazar 2020426180  "

#Problema: Construir una función que eleve un
#número entero x a una potencia n, sin utilizar el operador de exponente.

#E: dos números
#S: elevar x por la potencia n
#R: solo número enteros

def elevar(x, n):
     if isinstance(x, int) and isinstance(n, int) and n > 0 :
          return elevarAux(x, n, 1)
     else:
          return "error en la entrada"
#E: tres números
#S: elevar x por la potencia n
#R: no tiene

def elevarAux(x, n, res):
     if n == 0 :
          return res
     else:
          return elevarAux(x, n-1, res*x)
