import os
import sys

index=0
value=0
d=0

def Crear():
    queue=[0,0,0,0,0]
    index=0
    
    print("Cola creada exitosamente. ")
    input()
    return queue, index


queue, index = Crear()
print(queue)


def push( queue, value, index):
    try:
         
        if index <=0:                   #condicion en la que mientras el indice sea igual a cero, se agregaran los datos en ese indice
            queue[index]=value;          
            index+=1    
            return queue, value, index      #se regresan los valores de los parametros
        elif index ==1:                     #condicion en la que mientras el indice sea igual a cero, se agregaran los datos en ese indice
            queue[index]=value;          
            index+=1  
            return queue, value, index      #se regresan los valores de los parametros
        elif index ==2:                     #condicion en la que mientras el indice sea igual a cero, se agregaran los datos en ese indice
            queue[index]=value;          
            index+=1    
            return queue, value, index      #se regresan los valores de los parametros
        elif index ==3:                     #condicion en la que mientras el indice sea igual a cero, se agregaran los datos en ese indice
            queue[index]=value;          
            index+=1             
            return queue, value, index      #se regresan los valores de los parametros
        elif index ==4:                     #condicion en la que mientras el indice sea igual a cero, se agregaran los datos en ese indice
            queue[index]=value;          
            index+=1                    #incremento del indice                                   
            return queue, value, index      #se regresan los valores de los parametros
        else:                       #una vez se llenan los 5 espacios se imprime una advertencia de que no se puede formar mas gente
            print('*' * 25)
            print("La cola esta llena. ")
            print('*' * 25)
            return queue, value, index

    except:
        print("No existe cola, favor de crearla. ")
        input()
        return queue, value, index

def pop(queue,index):
    if index <0:
            print("La cola está vacía.")
     
    else:
            queue[0]=queue[1]               #se iguala el indice de la cola con su posterior para ir sacando sus elementos
            queue[1]=queue[2]               #y por lo tanto tener espacio para mas elementos
            queue[2]=queue[3]
            queue[3]=queue[4]
            queue[4]= 0
            index-=1
            print('*' * 25)
            print(queue)
            print('*' * 25)
            return queue,index
    
def Menu(queue, index):
    while True:
        
                 
        print("\nMenú")
        print("1.- Agregar elemento a la cola. ")
        print("2.- Sacar elementos de la cola. ")
        print("3.- Salir del programa. ")

        opc=int(input("¿Qué desea hacer? "))

        if opc==1:
                value=int(input("Ingrese un valor entero diferente de cero y diferente del anterior: "))
                queue, value, index = push(queue,value,index);
                print(queue)
        elif opc==2:
                queue, index = pop(queue, index);
                
                 
        elif opc==3:
                print("Fin del programa. ")
                sys.exit()
                         

Menu(queue, index)
