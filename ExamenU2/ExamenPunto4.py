#Delgado Vasquez Erik No.Matricula 172115151
import sys
ind=0       #se inicializa la variable del indice
value='Empty'       #se inicializa la variable del valor de cada ezpacio en la fila/cola

def new():      #creacion del metodo new
    fila=['Empty','Empty','Empty','Empty','Empty']      #creacion de la cola llamada fila
    ind=0
    return fila,ind     #se regresan los valores del indice y la fila para ser utilizados posteriormente


queue, ind = new()  #se crea el objeto del metodo new para utilizar la cola y almacenar datos
print('*' * 25)     #separador
print(queue)        #se imprime la fila

print('*' * 25)

def formar(queue, value, ind):      #creacion del metodo formar/push que recibe parametros de la cola, sus valores y el indice
    if ind ==0:                     #condicion en la que mientras el indice sea igual a cero, se agregaran los datos en ese indice
        queue[ind]=value;           
        ind+=1                      #incremento del indice
        print('*' * 25)                     
        print("El cliente se ha formado. ")     
        print('*' * 25)
        return queue, value, ind        #se regresan los valores de los parametros
    elif ind ==1:                   #se repite el mismo procedimiento, pero con el indice posterior 
        queue[ind]=value;
        ind+=1
        print('*' * 25)
        print("El cliente se ha formado. ")
        print('*' * 25)
        return queue, value, ind
    elif ind ==2:                   #se repite el mismo procedimiento, pero con el indice posterior 
        queue[ind]=value;
        ind+=1
        print('*' * 25)
        print("El cliente se ha formado. ")
        print('*' * 25)
        return queue, value, ind
    elif ind ==3:               #se repite el mismo procedimiento, pero con el indice posterior 
        queue[ind]=value;
        ind+=1
        print('-' * 25)
        print("El cliente se ha formado. ")
        print ('-' * 25)
        return queue, value, ind
    elif ind ==4:               #se repite el mismo procedimiento, pero con el indice posterior 
        queue[ind]=value;
        ind+=1
        print('*' * 25)
        print("El cliente se ha formado. ")
        print('*' * 25)
        return queue, value, ind
    else:                       #una vez se llenan los 5 espacios se imprime una advertencia de que no se puede formar mas gente
        print('*' * 25)
        print("La fila se ha llenado, espere a que alguien termine de pagar. ")
        print('*' * 25)
        return queue, value, ind


def pagar(queue, ind):          #creacion del metodo pagar/pop que recibe parametros de la cola y el indice
    queue[0]=queue[1]               #se iguala el indice de la colacon su posterior para ir sacando a las personas que van pagando
    queue[1]=queue[2]               #y por lo tanto tener espacio para que otros se formen
    queue[2]=queue[3]
    queue[3]=queue[4]
    queue[4]= 'Empty'               
    ind-=1                          #se decrese el indice para que sus valores vayan saliendo
    print('*' * 25) 
    print(queue)                        #se imprime la fila
    print('*' * 25)
    return queue, ind                   #regresa valores de la cola y el indice

def peek(queue,ind):                    #creacion del metodo peek que recibe valores de la cola y el indice
    if queue[0]=='Empty':               #condicion que dice, mientras el elemento con indice 0 de la cola sea igua a 'empty' 
        print('*' * 25)                     #se desplegara un mensaje advirtiendo que ya no hay gente formada
        print("No hay nadie formado. ")
        print('*' * 25) 
        return queue, ind                   #se devuelven valores de la cola y de; indice
    else:
        print('*' * 25)
        print(queue[0])                 #se imprimen los datos de la persona en el primer indice el cual es el '0'
        print('*' * 25)
        return queue, ind               # se devuelven valores de la cola y el indice

def peekAll(queue, ind):                #creacion del metodo peekAll que recibe parametros de la cola y el indice
    print('*' * 25)
    print(queue)                        #se encarga de imprimir toda la cola, para mostrar los datos de la gente formada
    print('*' * 25)
    return queue, ind                   #devuelve valores de la cola y el indice


def Tienda(queue, ind):                 #se crea el metodo tienda el cual es el menu y recibe parametros de la cola y el indice
    while True:
        print("MENU:")                                  
        print("1.- Meter un cliente en la fila. ")              #se da a elegir al usuario que es lo que quiere realizar
        print("2.- Mostrar primer cliente de la fila. ")
        print("3.- Cobrar al primer cliente. ")
        print("4.- Mostrar fila. ")
        print("5.- Salir del programa. ")
        print('*' * 25)
        k=int(input("¿Qué desea hacer? "))      #se pide al usuario ingrese su eleccion

        if k==1:                    #se crea la condicion, si la eleccion es igual a 1 se pide al usuario ingrese el nombre y numero del cliente
            value=str(input("""Ingrese "Nombre del cliente y su numero" para ingresarlo a la fila. """))
            queue, value, ind = formar(queue, value, ind);      # se mandan la cola, los datos ingresados y el indice al metodo a llamar, en este caso el metodo formar
            print(queue)                        # se imprime la cola
            print('*' * 25)
        else:
            if k==2:            #si la eleccion es 2
                queue, ind = peek(queue, ind); # se manda a llamar al metodo peek
            else:
                if k==3:                #si la eleccion es 3
                    queue, ind = pagar(queue, ind); #se manda a llamar al metodo pagar
                    if ind < 0:         #y se crea una condicion, si el indice es menor que cero se dice que la fila esta vacioa
                        print("La fila esta vacia. ")
                        print('*' * 25)
                else:
                    if k==4:    #si la eleccion es 4
                        queue, ind = peekAll(queue, ind);  #se manda a llamar al metodo peekAll
                    else:
                        if k==5:    #si la eleccion es 5
                            print("Fin del progama.")       #se finaliza el programa
                            sys.exit()


Tienda(queue, ind)
            
