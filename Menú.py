
global n
def Menu():

        print("1.- Imprimir 100 primeros números naturales. ")
        print("2.- Calcular factorial de un número. ")
        print("3.- Sucesión fibonacci de un número. ")
        print("4.- Salir")
        opcion = int(input ("Indique Opcion: "))
        if opcion == 1:
            cien=1
            NN(cien)
            Menu()
        else:
            if opcion==2:
                FactI()
                Menu()
            else:
                if opcion==3:
                    global n
                    n=int(input("Ingrese el número que desea sacar fibonacci: "))
                    for i in range (n):
                        print (fiboR(i))
                    
                    
                    Menu()
                else:
                    if opcion==4:
                        print("Fin del programa.")
                        exit
        

def NN(cien):
    if cien <=100:
        print (cien)
        NN(cien+1)
    else:
        print("End")




def FactI():
    número = int(input("Ingrese un número para obtener su factorial: "))

    factorial = int(1);
    print("Factorial de " + str(número) + ": ")
    for i in range(2, número+1):
        factorial = factorial*i
        print(factorial)


        #input()



def fiboR(n):  
    if n<=1:
        return 1
    else:
        return (fiboR(n-1) + fiboR(n-2))
        #n=int(input("Ingrese el número que desea sacar fibonacci: "))
        #print ("Fibonacci " + str(i+1) + " es: " + str(fiboR(i)))
    

Menu()


