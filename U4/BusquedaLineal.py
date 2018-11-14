import random
import sys
def listaAleatorios(n):
    global alist
    alist = [0]  * n
    for i in range(n):
        alist[i] = random.randint(0, 1000)
    return alist
def busqueda_lineal(lista, x):
    i = 0 # i tiene la posición actual en la lista, comienza en 0
    #El ciclo recorre todos los elementos de la lista
    for z in lista:
        # estamos en la posicion i, z contiene el valor de lista[i]
        #Si z es igual a x, devuelve el valor de i
        if z == x:
            print("\nEl elemento se encuentra en el indice: ",i)
            return i
        i = i+1
    print("\nEl elemento no se encuentra e la lista.")
            
    #si salió del ciclo sin haber encontrado el valor, devuelve -1
    return -1
print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
x=int(input("Ingrese el numero a buscar: "))
input()
busqueda_lineal(alist,x)
def DoAgain():
    print("\n¿Desea buscar otro elemento? \n1.-Si.\n2.-No.")
    opc=int(input())
    if opc==1:
        x=int(input("Ingrese el numero a buscar: "))
        busqueda_lineal(alist,x)
        DoAgain()
    elif opc==2:
        print("Fin del programa.")
        sys.exit()
DoAgain()
