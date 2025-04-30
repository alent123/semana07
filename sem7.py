# Challenge 1: Tree Height Calculation
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def altura(root):
    if root is None:
        return -1
    Izquierda = altura(root.left)
    Derecha = altura(root.right)
    return 1 + max(Izquierda, Derecha)

# Test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
altura_arbol = altura(root)
print("Altura del árbol:", altura_arbol)

# Challenge 2: Count Leaf Nodes
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def ContarHojas(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return ContarHojas(root.left) + ContarHojas(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print("Número de hojas:", ContarHojas(root))

# Challenge 3: Reflect a Binary Tree
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def reflejar(arbol):
    if arbol is None:
        return

    # Intercambiar los hijos izquierdo y derecho
    arbol.izquierdo, arbol.derecho = arbol.derecho, arbol.izquierdo

    # Aplicar recursivamente a los subárboles
    reflejar(arbol.izquierdo)
    reflejar(arbol.derecho)

# Función auxiliar para imprimir el árbol en preorden
def imprimir_preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        imprimir_preorden(nodo.izquierdo)
        imprimir_preorden(nodo.derecho)

# Ejemplo de uso
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

print("Árbol original (preorden):")
imprimir_preorden(raiz)

reflejar(raiz)

print("\nÁrbol reflejado (preorden):")
imprimir_preorden(raiz)

# Challenge 4: Level Order Traversal
import queue
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def recorrido(raiz):
    if raiz is None:
        return []
    resultado = []
    cola = queue.Queue()
    cola.put(raiz)

    while not cola.empty():
        actual = cola.get()
        resultado.append(actual.valor)
        if actual.izquierdo:
            cola.put(actual.izquierdo)
        if actual.derecho:
            cola.put(actual.derecho)

    return resultado

# Crear el árbol
raiz = NodoArbol(1)
raiz.izquierdo = NodoArbol(2)
raiz.derecho = NodoArbol(3)
raiz.izquierdo.izquierdo = NodoArbol(4)
raiz.izquierdo.derecho = NodoArbol(5)
raiz.derecho.derecho = NodoArbol(6)
print("Recorrido por niveles:", recorrido(raiz))

# Challenge 5: Check if a Binary Tree is Balanced
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def es_balanceado(nodo):
    def revisar(raiz):
        if raiz is None:
            return 0, True

        altura_izq, balanceado_izq = revisar(raiz.izq)
        altura_der, balanceado_der = revisar(raiz.der)

        altura_actual = 1 + max(altura_izq, altura_der)
        esta_balanceado = (
            balanceado_izq and
            balanceado_der and
            abs(altura_izq - altura_der) <= 1
        )

        return altura_actual, esta_balanceado

    _, resultado = revisar(nodo)
    return resultado

# Ejemplo: Árbol balanceado
raiz1 = Nodo(1)
raiz1.izq = Nodo(2)
raiz1.der = Nodo(3)
raiz1.izq.izq = Nodo(4)
raiz1.izq.der = Nodo(5)

# Ejemplo: Árbol no balanceado
raiz2 = Nodo(1)
raiz2.izq = Nodo(2)
raiz2.izq.izq = Nodo(3)
raiz2.izq.izq.izq = Nodo(4)

print("¿Árbol 1 está balanceado?", es_balanceado(raiz1))  # True
print("¿Árbol 2 está balanceado?", es_balanceado(raiz2))  # False
