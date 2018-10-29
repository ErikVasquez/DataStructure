import os
import sys

class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None

class Rorschach(): 
    
    def __init__(self): 
        self.root = None 
        self.due = None
        self.end=None

    
    def Null(self): 
        if self.root == None: 
            return True 
        else:
            return False

    def Lpush(self,data):
        if self.Null() == True: 
            self.root = self.due = Node(data) 
        else:
            temp = Node(data)
            temp.next = self.root
            self.root.prev = temp
            self.root = temp
        
    def Rpush(self,data):
        if self.Null() == True: 
            self.root = self.due = Node(data) 
        else:
            temporal = self.due
            self.due = temporal.next = Node(data)
            self.due.prev = temporal

    def Lpeek(self):
        mushu = self.root
        if self.Null() == True:
            print("\nNo hay datos en la lista.")
        else:
            while mushu:
                print("["+ str(mushu.data)+"]")
                mushu = mushu.next

    def Rpeek(self):
        mushu = self.due
        if self.Null() == True:
            print("No hay atos en la lista.")
        else:
            while mushu:
                print("["+ str(mushu.data)+"]")
                mushu = mushu.prev

    def Search(self, item):
        temp = self.root
        i = False
        while temp:
            if temp.data ==item:
                i = True
                return i
            else:
                temp = temp.next
                if temp == self.root:
                    i = False
                    return i

    def RErase(self):
        if self.Null() == True:
            print("\nNo hay ninguna raiz para ser eliminada.")
        elif self.root.next == None:
            self.root = self.due = None
            print("\nUnica raiz eliminada exitosamente.")
        else:
            self.root = self.root.next
            self.root.prev = None
            print("\nLa raiz ha sido eliminada. ")

    def Erase(self):
        if self.Null() == True:
            print("\nNo existen datos que puedan ser eliminados.")
        elif self.root.next == None:
            self.root = self.due = None
            print("\nElemento final eliminado exitosamente.")
        else:
            self.due = self.due.prev
            self.due.next = None
            print("\nEl dato ha sido eliminado exitosamente. ")

    def SErase(self,item):
        
        self.due = self.root 
        temp = 1 
        
        if self.Null() == True: 
            print("\nLa lista esta vacia")
        else:
            while self.due.data != item and temp == 1:
                if self.due.next != self.root:
                    self.end = self.due
                    self.due = self.due.next 
                else:
                    temp = 0
        
            if temp == 0: 
                print("\nNo existe el elemento que desea eliminar")
            else:
                if self.root == self.due:  
                    self.root = self.due.next
                else:
                    self.end.next=self.due.next
                    self.due = None 
                    print("\nDato eliminado correctamente")

class  Menu(): 
    
    def __init__(self): 
        self.op = None
        
    def fill(self): 
        filled = Rorschach() 
        while True: 
            print("\n1.-Ingresar datos por izquierda\n2.-Ingresar datos por derecha\n3.-Mostrar datos por la izquierda\n4.-Mostrar datos por la derecha\n5.-Buscar dato\n6.-Eliminar Datos\n7.-Eliminar raiz\n8.-Buscar y eliminar un dato\n9.-Salir")
            self.op = int(input("\nIngrese opcion: ")) 
            os.system("clear")
            
            if self.op == 1:
                data = input("\nIngrese dato: ")
                filled.Lpush(data)
                
            elif self.op == 2:
                data = input("\nIngrese dato: ")              
                filled.Rpush(data)

            elif self.op == 3:
                filled.Lpeek()

            elif self.op ==4:
                filled.Rpeek()

            elif self.op ==5:
                data = input("\nIngrese el dato que desea buscar: ")
                check = filled.Search(data)
                if check == True:
                    print("\nEl dato existe en la lista.")
                else:
                    print("\nEl dato no existe en la lista.")
                    
            elif self.op == 6:
                filled.Erase()

            elif self.op == 7:
                filled.RErase()

            elif self.op == 8:
                data = input("\nIngrese el dato que desee eliminar: ")
                filled.SErase(data)
    
            elif self.op == 9:
                sys.exit() 
                
            else: 
               print("\nOpcion invalida.")
            


Imprimir = Menu()
Imprimir.fill()
