import random
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
    print("Merging ",alist)

print("Ingrese cuantos numeros aleatorios desea obtener")
alist=int(input())
aleatorios=listaAleatorios(alist)
print(aleatorios)
input()
mergeSort(alist)
print(alist)
