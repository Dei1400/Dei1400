" Portafolio 3  |  Deilyn Salazar Murillo 2020426180 "

#sumatoria de un número

#E: Un número
#S: sumatoria del numerp ingresado
#R: num entero
def sumatoria(num):
    if isinstance(num,int):
        res = 0
        if num < 0: #nums negativos
            num *= -1 #cambia signo
        while num > 0:
            res += num
            num -= 1
        return res
    else:
        return -1 #error en la emtrada
