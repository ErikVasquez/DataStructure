#Delgado Vasquez Erik No.Control 17211515
import random
def listaAleatorios(n):         #se crea el metodo del cual se obtendra un arreglo de elementos completamente aleatorios
    global alist        #se crea la variable global alist
    alist = [0]  * n        #se multiplica un arreglo con un elemento 0 por el numero de datos solicitados
    for i in range(n):          #se crea un for donde 
        alist[i] = random.randint(0, 1000)      #se creara un arreglo completamente aleatorio entre los numeros escogidos
    return alist                    #se devuelve el arreglo
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
print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
cobra=shellSort(alist)
print("Presione cualquier letra para imprimir la lista ordenada de menor a mayor.")
input()
print(alist)
    
