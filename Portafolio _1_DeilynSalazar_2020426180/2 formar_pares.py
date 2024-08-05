" Portafolio #1  | Deilyn Salazar 2020426180 "

# 2 FORMAR UN NÚMERO CON PARES

#E: Un número
#S: Formar un nuevo número con los digitos pares de la entrada
#R: solo números enteros
#(CUENTA LA CERO COMO PAR)

def formar_pares(num):
     if isinstance(num, int):
          if num < 0 :
               return formar_pares(num*-1) #multiplicar por menos uno para manejar solo positivos
          if num == 0 : #para que cuente el 0 como par
               return 1
          else:
               return formar_pares_aux(num, 0)#a la nueva función s ele manda un cero para manejar las potencias
     else:                                    # a la hora de formar en nuevo número (num * 10 ** p)
          return -1 #Mensaje de error en la entrada
#E: Dos números
#S: Formar un nuevo número con los digitos pares de la entrada
#R: no tiene

def formar_pares_aux(num, p):
     if num == 0 : #este cero no es del número de la entrada
          return 0
     elif num == 1: #condiciones de parada
          return 0
     elif (num%10)%2 == 0 : #se saca el ultimo número y si el modulo de dos es igual a cero es un número par
          return num%10 * 10 ** p + formar_pares_aux(num//10, p+1) #se le suma uno a p para la siguiente posición
                 #se saca el ultimo número se multiplica por diez a la potencia de p 
     else :
          return formar_pares_aux(num//10, p)
                 #se corta el ultimo digito pero no se le suma a p porque no se ocupo la posción
