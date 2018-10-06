#Delgado Vasquez Erik No.Matricula 172115151
import sys


class proyecto():  #se crea el metodo proyecto
    stack=[]        #se inicializa la pila

    def Crear(self):    #se crea el metodo crear, en el cual, como su nombre lo dice, se crea la pila
        self.stack=[]
        print("Proyecto creado exitosamente. ")
        input()

    def push(self):         #creacion del metodo push
        try:
            n=float(input("Ingrese numero de migracion: "))     #se pidel al usuario ingrese el numero de migracion del proyecto
            self.stack.append(n)                                #Nota: con numero de migracion nos referimos a la actualizacion del proyecto
            print("Migracion ingresada. ")                      #Ejemplo: Migracion 1.75, migracion 1.79, migracion 2.0, etc.
            input()

        except:
            print("No existe proyecto, favor de crearlo. ")     #se pone una excepcion, la cual nos pedira que se cree un proyecto en caso de que
            input()                                             #el usuaio quiera ingresar migraciones sin existir un proyecto

    def peek(self):                                 #creacion del metodo peek
        if 0 < len(self.stack):                     #condicion que nos permitira ingresar migraciones mientras la longitud de la pila sea mayor que cero
            print(self.stack[len(self.stack)-1])     #se imprime la ultima migracion realizada
            self.stack.pop()                        #saca la migracion que se encuentra en el ultimo lugar, para despues mostrar la migracion anterior a esta ultima
            input()
        else:
            print("No hay migraciones para mostrar. ") #En cso de que se hayan mostrado todas las migraciones
                                                        #se pone una advertencia de que ya no hay migraciones mas antiguas y no se puede mostrar nada
    def size(self):                    #creacion del metodo size
        print(len(self.stack))          #se imprime la longitud de la pila, el numero de migraciones ingresadas

    def Migraciones(self):          #creacion del metodo migraciones
        print(self.stack)           #se muestran todas las migraciones que haya existentes en el proyecto
        print("Migraciones ingresadas del proyecto. ")

    
                 
stack=proyecto() #se crea el objeto stack para ser utilizado posteriormente


while True:
         
    print("Menú")                                       #creacion del menu para dar a elegir al usuario que desea hacer
    print("1.- Crear un proyecto. ")                    #se debe crear obligatoriamente el proyecto para seguir utilizando el programa
    print("2.- Introducir migracion. ")
    print("3.- Obtener migracion. ")
    print("4.- Saber numero de migraciones. ")
    print("5.- Mostras todas las migraciones. ")
    print("6.- Salir del programa. ")

    opc=int(input("¿Qué desea hacer? "))        #lectura de la opcion tomada por el usuario
    if opc==1:              
        stack.Crear()           #se manda a llamar al metodo crear
    else:
        if opc==2:
            stack.push()        #se manda a llamar ak metodo push para ingresar migraciones al proyecto
        else:
            if opc==3:
                stack.peek()        #se manda a llamar al metodo peek apra mostrar la ultima migracion
            else:
                if opc==4:
                    stack.size()        #se manda a llamar al metodo size para saber cuantas migraciones hay existentes en el proyecto
                else:
                    if opc==5:
                        stack.Migraciones()     #se manda a llamar al metodo migraciones para mostrar todas las migraciones existentes en el proyecto
                    else:
                        if opc==6:
                            print("Fin del programa. ") 
                            sys.exit()                  #se finaliza el programa
