import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Rorschach:
    def __init__(self):
        self.root=None
        self.nigel=None
        self.memo=None
    def kuki(self,data):
        pixie=True
        if self.root==None:
            morph=Node(data)
            self.root=morph
            self.nigel=morph
        else:
            while pixie==True:
                if self.nigel.left==None and self.nigel.right==None:
                    print("No hay nodos del lado derecho y del lado izquierdo.")
                elif self.nigel.left !=None and self.nigel.right==None:
                    print("Existe un nodo en el lado izquierdo con el dato: "+str(self.nigel.left.data)+", no hay nodos del lado derecho.")
                elif self.nigel.left==None and self.nigel.right!=None:
                    print("No hay nodos del lado izquierdo, existe un nodo del lado derecho con el dato: "+str(self.nigel.right.data))
                elif self.nigel.left!=None and self.nigel.right!=None:
                    print("Existe un nodo del lado izquierdo con el dato: "+str(self.nigel.left.data)+ " y un nodo del lado derecho con el dato: " +str(self.nigel.right.data))
                way=int(input("Ingrese a que lado desea ingresar el valor.\n1.-A la izquierda\n2.-A la derecha. "))
                if way==1 and self.nigel.left==None:
                    morph=Node(data)
                    self.nigel.left=morph
                    self.nigel=self.root
                    pixie=False
                elif way==1:
                    self.nigel=self.nigel.left
                if way==2 and self.nigel.right==None:
                    morph=Node(data)
                    self.nigel.right=morph
                    self.nigel=self.root
                    pixie=False
                elif way==2:
                    self.nigel=self.nigel.right
    def Inorden(self,nodo,string):
        if nodo:
            self.Inorden(nodo.left,string)
            print((nodo.data))
            self.Inorden(nodo.right,string)
    def do(self):
        yao=self.root
        print(self.Inorden(yao,""))
        
Tree=Rorschach()
while True:
    print("-----MENU-----")
    print("\n1.-Ingresar nuevo nodo.\n2.-Recorrido Inorden.\n3.-Salir")
    choice=int(input("¿Qué desea hacer? "))
    if choice ==1:
        data=int(input("Ingrese el dato: "))
        Tree.kuki(data)
    elif choice==2:
        Tree.do()
    elif choice==3:
                 sys.exit()
        
