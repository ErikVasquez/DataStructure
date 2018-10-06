#Delgado Vasquez Erik No.Matricula 172115151
import sys
global a

global n
def potencia(a,n): #se crea el metodo potencia que recibe dos parametros
    if (n ==0):    #se crea la condicion donde si el valor de "n" es "0" regresara como resultado "1"
        return 1
    
    else:
        return a * potencia(a, n-1)  #En caso contrario realizara la operacion debida para dar el resultado de la funcion

global a
a=2

global n # se crea una variable glonal "n"
try:    #se crea un try para ingresar el valor del exponencial
    n=int(input("Ingrese el valor de la potencia: "))
except ValueError:  #si el termino ingresado no es un entero saltara la excepcion 
    print("Ingrese un dato valido. ")
else:
    print("El resultado de la funcion es: " + str(potencia(a,n))) #si el valor ingresado es valido se imprime el resultado


def repetir():          #se crea el metodo repetir para que el usuario elija si quiere realizar la funcion con otro valor del exponente
    print("1.-Utilizar otro exponente. ")
    print("2.-Salir del programa. ")
    r=int(input("¿Qué desea hacer?. ")) #se pregunta al usuario su decision 
    if r==1:
        a=2                     #si la opcion es la primera se repite el proceso de capturar el exponente e imprimir el resutlado
        try:
            n=int(input("Ingrese el valor de la potencia: "))
        except ValueError:
            print("Ingrese un dato valido. ")
            repetir()
        else:
            print("El resultado de la funcion es: ", potencia(a,n))
            repetir()
    
    else:                       #en caso contrario se imprime el texto "Fin del programa" y termina el mismo.
        if r==2:
            print("Fin del programa.")
            sys.exit()
        else:
            print("Opción incorrecta, introduzca una opción válida.¨")      #Si el usuario ingresa una opcion que no se encuentra en el menu salta 
            input()                                                         #la advertencia y le pide ingresar datos existentes
            repetir()

repetir()
