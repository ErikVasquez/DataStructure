#Delgado Vasquez Erik No.Matricula 172115151
def suma(n):        #Se crea el metodo suma
    if (n==1):          #se crea la condicion
        return 1        #si el valor de n fuese "1" se regresaria el valor de "1"
    else:
        return n+suma(n-1)      #En caso contrario, se suma el valor de "n" 
                                #con el valor anterior a el mismo, esto
n=9                             #mandando a llamar a su mismo metodo por medio de recursividad
print("La suma de 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 es de: "+ str(suma(n))) #se imprime la suma de los numeros
