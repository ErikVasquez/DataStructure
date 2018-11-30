#Delgado Vasquez Erik
from math import log10
from random import randint
import random
import time                     #se importan las librerias necesarias para la correcta ejecucion del programa
import sys
import timeit
global find
global mushu
global alist
def listaAleatorios(n):         #se crea el metodo del cual se obtendra un arreglo de elementos completamente aleatorios
    global alist        #se crea la variable global alist
    alist = [0]  * n        #se multiplica un arreglo con un elemento 0 por el numero de datos solicitados
    for i in range(n):          #se crea un for donde 
        alist[i] = random.randint(0, 1000)      #se creara un arreglo completamente aleatorio entre los numeros escogidos
    return alist                    #se devuelve el arreglo
def mergeSort(alist):           #metodo merge, recibe como parametro lel arreglo para acomodarlo posteriormente
    if len(alist)>1:
        mid = len(alist)//2         #se divide a la mitad el arreglo
        lefthalf = alist[:mid]      #se asignan los dos arreglos a las variables lefthalf y righthalf
        righthalf = alist[mid:]
        mergeSort(lefthalf)         
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf): #mientras i sea menor que la longitud de el arreglo ixquierdo y j es menor que la longitud del arreglo derecho entonces
            if lefthalf[i] < righthalf[j]: #si el arreglo izquierdo es menor que el derecho
                alist[k]=lefthalf[i]        #se guarda el valor de i del arreglo izquierdo en la lista con la variable k
                i=i+1                       #i se iguala a i+1 para aumentar el contador
            else:
                alist[k]=righthalf[j]       #se guarda el valor de j del arreglo izquierdo en la lista con la variable k
                j=j+1                       #j se iguala a j+1 para aumentar el contador
            k=k+1       
        while i < len(lefthalf):            #mientras i sea menor que la longitud del arreglo izquierdo
            alist[k]=lefthalf[i]                #se guarda el valor de i del arreglo dereho en la lista con la variable k
            i=i+1
            k=k+1
        while j < len(righthalf):           # mientras j sea menor que la longitud del arreglo derecho
            alist[k]=righthalf[j]           #se guarda el valor de j del arreglo dereho en la lista con la variable k
            j=j+1
            k=k+1
def shellSort(alist):               #metodo shellsort, recibe como parametro lel arreglo para acomodarlo posteriormente
    gap=len(alist)//2               #se divide el arreglo entre 2
    while gap>0:                        #mientras la variable gap sea mayor que 0 entonces
        for i in range(gap,len(alist)):     #se crea un for desde el valor de gap hasta el largo del arreglo
            val=alist[i]                    #se guarda el valor de i de =l arreglo en la varaible val
            j=i                             #se iguala i a j
            while j >= gap and alist[j-gap]>val:        #mientras j sea mayor o igual a gap y el valor del arreglo menos gap sea mayor al valor entonces
                alist[j]=alist[j-gap]               #se guarda el valor de la j menos el valor de gap en el arreglo en j
                j-=gap                              #se va disminuyendo el valor de gap
            alist[j]=val                            #se guarda el valor de val e el arreglo en j
        gap//=2                                 

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
def Bubbles(lista):             #metodo burbuja, recibe como parametro el arreglo para acomodarlo posteriormente
    bubble=0
    for i in range (0,len(lista)):      #se meten en un for el arreglo que va desde 0 hasta el largo del arreglo
        for j in range (0,len(lista)-1): #se crea un for desde 0 asta el penultimo valor del largo del arreglo
            if lista[j]>lista[j+1]:         #si la lista en j es mayor qe el siguiente valor en la lista entonces
                bubble=lista[j+1]           #se iguala la bariable bubble el valor siguiente de j
                lista[j+1]=lista[j]         #se guarda en dato de j en el dato siguiente de j
                lista[j]=bubble             #se guarda el dato de bubble en j
def pruebas():                  #metodo pruebas, aqui se realizaran las pruebas de cada metodo, utilizando el mismo arreglo con cada metodo, pero diferetne arreglo cada prueba.
    global alist
    for j in range(1,31):       #se crea un for donde se realizara cada metodo hasta completar las 30 puebas
        alist=500
        aleatorios=listaAleatorios(alist)
        print(aleatorios)           #se manda a llamar el metodo aleatorios, que es donde se creara el arreglo con una cantidad de 500 elementos aleatorios
        print("\nPrueba ",j,".\n")
        starting_point=time.perf_counter() #se crea la variable para guardar el tiempo de ejecucion antes de llamar el metodo
        Bubbles(alist)                      #se manda a llamar al metodo
        print(alist)                        #se imprime el arreglo ya ordenado
        last=time.perf_counter()                #se crea la variable para guardar el tiempo de ejecucion despues de llamar al metodo
        elapsed_time=(last-starting_point)*1000 #se restan y se multiplican por 1000 para mostrar el resultado en milisegundos
        print("\nTiempo transcurrido BubbleSort: %.5f milisegundos." % elapsed_time) #se imprime el tiempo de ejecucion en milisegundos
        starting_point=time.perf_counter()   #se crea la variable para guardar el tiempo de ejecucion antes de llamar el metodo
        quickSort(alist)        #se manda a llamar al metodo
        print(alist)         #se imprime el arreglo ya ordenado
        last=time.perf_counter()            #se crea la variable para guardar el tiempo de ejecucion despues de llamar al metodo
        elapsed_time=(last-starting_point)*1000         #se restan y se multiplican por 1000 para mostrar el resultado en milisegundos
        print("\nTiempo transcurrido QuickSort: %.5f milisegundos." % elapsed_time)#se imprime el tiempo de ejecucion en milisegundos
        starting_point=time.perf_counter()       #se crea la variable para guardar el tiempo de ejecucion antes de llamar el metodo
        shellSort(alist)            #se manda a llamar al metodo
        print(alist)             #se imprime el arreglo ya ordenado
        last=time.perf_counter()            #se crea la variable para guardar el tiempo de ejecucion despues de llamar al metodo
        elapsed_time=(last-starting_point)*1000     #se restan y se multiplican por 1000 para mostrar el resultado en milisegundos
        print("\nTiempo transcurrido ShellSort: %.5f milisegundos." % elapsed_time)#se imprime el tiempo de ejecucion en milisegundos
        starting_point=time.perf_counter()       #se crea la variable para guardar el tiempo de ejecucion antes de llamar el metodo
        mergeSort(alist)            #se manda a llamar al metodo
        print(alist)             #se imprime el arreglo ya ordenado
        last=time.perf_counter()            #se crea la variable para guardar el tiempo de ejecucion despues de llamar al metodo
        elapsed_time=(last-starting_point)*1000#se restan y se multiplican por 1000 para mostrar el resultado en milisegundos
        print("\nTiempo transcurrido ShellSort: %.5f milisegundos." % elapsed_time)#se imprime el tiempo de ejecucion en milisegundos
pruebas()
