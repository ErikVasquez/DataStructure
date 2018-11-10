#Delgado Vasquez Erik No.Control 17211515
import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Rorschach:
    def __init__(self):
        self.root=None
        self.uno=None
    def sanik(self,data):
        arrow=True
        if self.root==None:
            morph=Node(data)
            self.root=morph
            self.uno=morph
        else:
            while arrow==True:
                if data<self.uno.data and self.uno.left==None:
                    morph=Node(data)
                    self.uno.left=morph
                    self.uno=self.root
                    arrow=False
                elif data<self.uno.data and self.uno.left!=None:
                    self.uno=self.uno.left
                elif data>=self.uno.data and self.uno.right==None:
                    morph=Node(data)
                    self.uno.right=morph
                    self.uno=self.root
                    arrow=False
                elif data>=self.uno.data and self.uno.right!=None:
                    self.uno=self.uno.right
    def Do(self,t):
        yao=self.root
        if t=="Inorden":
            print(self.Inorden(yao))
        if t=="PreOrden":
            print(self.PreOrden(yao))
        if t=="PostOrden":
            print(self.PostOrden(yao))
    def Inorden(self,node):
        if node:
            self.Inorden(node.left)
            print(node.data)
            self.Inorden(node.right)
    def PreOrden(self,node):
        if node:
            print(node.data)
            self.PreOrden(node.left)
            self.PreOrden(node.right)
    def PostOrden(self,node):
        if node:
            self.PostOrden(node.left)
            self.PostOrden(node.right)
            print(node.data)
Xmas=Rorschach()
while True:
    print("\t\t-----MENU-----")
    print("\n1.-Ingresar nodo.\n2.-Recorrido Inorden.\n3.-Recorrido PreOrden\n4.-Recorrido PostOrden.\n5.-Salir.")
    opc=int(input("Ingrese opcion: "))
    if opc==1:
        n=int(input("Ingrese elemento: "))
        Xmas.sanik(n)
    elif opc==2:
        Xmas.Do("Inorden")
    elif opc==3:
        Xmas.Do("PreOrden")
    elif opc==4:
        Xmas.Do("PostOrden")
    elif opc==5:
        sys.exit()
