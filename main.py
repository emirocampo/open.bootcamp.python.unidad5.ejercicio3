def bisiesto(anio):
    if(anio % 4 != 0):
        return "no es bisiesto"
    elif(anio % 4 == 0 and anio % 100 != 0):
        return "es bisiesto"
    elif(anio % 4 ==0 and anio % 100 == 0 and anio % 400 != 0):
        return "no es bisiesto"
    elif(anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0):
        return "es bisiesto"


print(bisiesto(2000))
print(bisiesto(1998))
print(bisiesto(2006))
    