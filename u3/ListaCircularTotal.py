import os
import sys
class Node(): 
    def __init__(self, data):
        self.data = data 
        self.next = None 
    
        
class Rorschach(): 
    
    def __init__(self): 
        self.root = None 
        self.end = None 
        self.ended = None 
    
    def Null(self): 
        if self.root == None: 
            return True 
        else:
            return False 
        
    def push(self,data): 
        
        if self.Null() == True: 
            self.root = self.end = self.ended = Node(data)
            self.end.next = self.root
        else:
            temporal = self.ended 
            self.end = self.ended = temporal.next = Node(data)
            self.end.next = self.root
            
    def peek(self): 
        temp = self.root
        i = True
        if self.Null() == True: 
            print("\nNo hay datos registrados...") 
        else:
            while i: 
                print("[" + str(temp.data)+"] ")
                if temp ==self.ended:
                    i = False
                else:
                    temp = temp.next 
    
    def Search(self,item):
        self.end = self.root
        temp = 1
        if self.Null() == True:
                    print("\nLa lista esta vacia.")
        else:
                    
            while self.end.data != item and temp ==1:  
                if self.end.next != self.root:  
                    self.end = self.end.next 
                else:
                    temp = 0
                if temp == 0:
                        print("\nNo existe el dato en la lista.")
                else:
                        print("\nEl dato existe en la lista.")
    
    def RErase(self): 
        temp = self.root 
        if self.Null() == False: 
            self.root = self.root.next
            self.end.next = self.ended.next = self.root
            temp = None 
        else: 
            print("\nNo existe raiz en la lista para eliminar.")
        
    def Erase(self): 
        self.end = self.root 
        temp = self.end 
        if self.Null() == False: 
            if temp != self.ended: 
                while temp.next != self.ended: 
                    temp = temp.next 
                temp.next = None 
                self.ended = temp
                self.end.next = self.ended.next = self.root
            else:
                self.root = None 
        else:
            print("\nNo hay datos en la lista para eliminar.")
            
    def SErase(self,item): 
        self.end = self.root 
        temp = 1 
        
        if self.Null() == True: 
            print("\nLa lista esta vacia")
        else:
            while self.end.data != item and temp == 1:
                if self.end.next != self.root: 
                    self.ended = self.end   
                    self.end = self.end.next 
                else:
                    temp = 0
        
            if temp == 0: 
                print("\nNo existe el elemento que desea eliminar")
            else:
                if self.root == self.end:  
                    self.root = self.end.next
                else:
                    self.ended.next = self.end.next
                self.end = None 
                print("\nDato eliminado correctamente")

class  Menu(): 
    
    def __init__(self): 
        self.op = None
        
    def fill(self):
        filled = Rorschach() 
        while True: 
            print("\n1.-Guardar datos\n2.-Eliminar raiz\n3.-Eliminar Elemento\n4.-Buscar y eliminar\n5.-Mostrar datos\n6.-Buscar dato\n7.-Salir")
            self.op = int(input("\nIngrese opcion: ")) 
            os.system("clear") 
            
            if self.op == 1:
                x = input("\nIngresa dato: ")
                filled.push(x)
            
            elif self.op == 2:
                filled.RErase() 
                
            elif self.op == 3:
                filled.Erase()
            elif self.op == 4:
                data = input("\nIngresa dato a eliminar: ")
                filled.SErase(data) 
                
            elif self.op == 5:
                filled.peek() 
            
            elif self.op == 6:
                data = input("\nIngresa dato a buscar: ")
                check = filled.Search(data) 
                
                    
            elif self.op == 7:
                sys.exit() 
                
            else: 
                print("\nOpcion invalida")


Imprimir = Menu() 
Imprimir.fill() 
