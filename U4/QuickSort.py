#Delgado Vasquez Erik No.Control 17211515
import random
def listaAleatorios(n):         #se crea el metodo del cual se obtendra un arreglo de elementos completamente aleatorios
    global alist        #se crea la variable global alist
    alist = [0]  * n        #se multiplica un arreglo con un elemento 0 por el numero de datos solicitados
    for i in range(n):          #se crea un for donde 
        alist[i] = random.randint(0, 1000)      #se creara un arreglo completamente aleatorio entre los numeros escogidos
    return alist                    #se devuelve el arreglo
def quickSort(alist):           #metodo quicksort, recibe como parametro el arreglo para acomodarlo posteriormente
   quickSortHelper(alist,0,len(alist)-1) #se manda a llamar al metodo helper con los parametros del arreglo, el 0 que sera el primer valor y el largo del arreglo que sera el ultimo
def quickSortHelper(alist,first,last):      #metodo helper
   if first<last:   #si el primer valor es menor que el ultimo entonces 
       splitpoint = partition(alist,first,last)         #se crea la variable splitpoint en la que se guarda lo que devuelve el metodo partition 
       quickSortHelper(alist,first,splitpoint-1)            #se llama el metodo con los parametros del arreglo, el primer valor y el anterior al splitpoint
       quickSortHelper(alist,splitpoint+1,last)     #se llama el metodo con los parametros del arreglo, el siguiente al splitpoint y el ultimo valor
def partition(alist,first,last):    #metodo partition con los parametros del arreglo, el primer y ultimo valor.
   pivotvalue = alist[first]        #se crea un pivote y se le asigna el primer valor del arreglo
   leftmark = first+1               # se crea un puntero izquierdo y toma el segundo valor del arreglo
   rightmark = last                 #se crea un puntero derecho y toma el ultimo valor del arreglo
   done = False                     #se le da valor False a la variable done
   while not done:                  #mientras que done no sea False
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:       #mientras que el puntero izq sea menor o igual al derecho y el valor del puntero
           leftmark = leftmark + 1                                          #izq en el arreglo sea menor o igual al pivote entonces el puntero izq toma el
                                                                            #siguiente valor
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:      #mientras el valor del puntero derecho en el arreglo sea mayor o igual al pivote y
           rightmark = rightmark -1                         # el puntero derecho sea menor o igual al puntero derecho entonces el puntero derecho toma el
                                                            #valor anterior a este
       if rightmark < leftmark:             #si el puntero derecho es menor que el izquierdo done devuelve valor True
           done = True
       else:        #en caso contrario, se crea una variable temp, y se le asigna el valor del puntero izquierdo en el arreglo 
           temp = alist[leftmark]               
           alist[leftmark] = alist[rightmark]   #se guarda el valor del puntero derecho en el arreglo en el puntero izquierdo
           alist[rightmark] = temp      #y se guarda el valor de temp en el puntero derecho del arreglo
   temp = alist[first]      #se guarda el primer vaor del arreglo en la variable temp
   alist[first] = alist[rightmark]          #se guarda el valor del puntero derecho en el arreglo en el primer valor del arreglo
   alist[rightmark] = temp      #se guarda el valor de temp en el punteroderecho del arreglo
   return rightmark             #devuelve el valor del puntero derecho

print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
cobra=quickSort(alist)
print("Presione cualquier letra para imprimir la lista ordenada de menor a mayor.")
input()
print(alist)

