" Portafolio #1 | Deilyn Salazar 2020426180 "

# 3 POTENCIA

#E: Dos númeors
#S: El primeor elevado por el segundo
#R: Enteros positivos

def potencia(x, n):
     if isinstance(x, int) and isinstance(n, int) and n >= 0 and x >= 0 :
          if n == 0 :
               return 1
          else:
               return x * potencia(x, n-1)
