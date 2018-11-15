#Delgado Vasquez Erik   No.Control 17211515
import random   
import sys      #se importan random y sys para obtener una lista con elementos aleatorios y salir del programa respectivamente
global find
global mushu
def listaAleatorios(n):     #se crea el metodo donde se obtendra el arreglo con elementos
    global alist
    alist = [0]  * n
    for i in range(n):
        alist[i] = random.randint(0, 1000)
    return alist
def quickSort(alist):               #se crea un metodo de quicksort para ordenar la lista, ya que es necesario para el metodo de busqueda binaria
   quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
   if first<last:
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark
def BusquedaBinaria(lista,x):       #metodo de busqueda binaria
    find=False      #se crea una valiable que se utilizara para darle valores True o False
    mushu=0         #un puntero se crea 
    Arraylen=len(lista)     #se asigna la longitud del arreglo a una variable
    while not(find) and mushu <= Arraylen:      #se dice que mientras el el valor de find no sea False y el puntero sea menor a la longitud del array
        half = int((mushu+Arraylen) / 2)        #se creara una variable donde se almacenara el valor de la mitad del puntero y la longitud del array
        if x == lista[half]:                    #mientras el valor de x sea igual al indice que se encuentra al valor de la mitad del vector    
            find = True                         #regresara valor True
        elif x < lista[half]:                   #en caso contrario, si la x es menor al valor del indice se asigna el valor anterior al array
            Arraylen = half - 1
        else:                                   #de otra forma, se asigna el valor siguiente al puntero
            mushu = half + 1      
    if find:
        print("El dato se encuentra en la posicion: ", str(half+1)) #si el valor de find es true, imprime el indice en que se encuentra
    else:
        print("El dato no existe en el arreglo.")       #en caso contrario, indica que no existe.
print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
sanik=quickSort(alist)
print("Lista ordenada:\n",alist)
input()
x=int(input("Ingrese el numero a buscar: "))
input()
BusquedaBinaria(alist,x)    
def DoAgain():      #se hace un pequeño menu en el que se lepregunta al usuario d=si desea buscar otro elemento del mismo arreglo.
    print("\n¿Desea buscar otro elemento? \n1.-Si.\n2.-No.")
    opc=int(input())
    if opc==1:
        x=int(input("Ingrese el numero a buscar: "))
        BusquedaBinaria(alist,x)
        DoAgain()
    elif opc==2:
        print("Fin del programa.")
        sys.exit()
DoAgain()
