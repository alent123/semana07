# ==========================================================
# Lab 07 - Binary Trees
# Algoritmos y Estructuras de Datos
# Autor(es): [Nombre del integrante 1], [Nombre del integrante 2], [Nombre del integrante 3]
# ==========================================================

# ---------------------------
# Challenge 1: Tree Height Calculation
# ---------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def altura(root):
    """
    Calcula la altura de un árbol binario.
    Retorna -1 si el árbol está vacío.
    """
    if root is None:
        return -1
    izquierda = altura(root.left)
    derecha = altura(root.right)
    return 1 + max(izquierda, derecha)

# Árbol de ejemplo
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print("\n--- Challenge 1 ---")
print("Altura del árbol:", altura(root1))
print("Árbol vacío:", altura(None))
print("Árbol con un solo nodo:", altura(TreeNode(10)))

# ---------------------------
# Challenge 2: Count Leaf Nodes
# ---------------------------

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def contar_hojas(root):
    """
    Cuenta los nodos hoja en un árbol binario.
    """
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return contar_hojas(root.left) + contar_hojas(root.right)

# Árbol de ejemplo
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)

print("\n--- Challenge 2 ---")
print("Número de hojas:", contar_hojas(root2))
print("Árbol vacío:", contar_hojas(None))
print("Árbol con un nodo:", contar_hojas(TreeNode(8)))

# ---------------------------
# Challenge 3: Tree Mirroring
# ---------------------------

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def reflejar(arbol):
    """
    Refleja (espeja) el árbol binario intercambiando los hijos.
    """
    if arbol is None:
        return
    arbol.izquierdo, arbol.derecho = arbol.derecho, arbol.izquierdo
    reflejar(arbol.izquierdo)
    reflejar(arbol.derecho)

def imprimir_preorden(nodo):
    """
    Imprime el árbol en preorden para visualizar el resultado.
    """
    if nodo:
        print(nodo.valor, end=' ')
        imprimir_preorden(nodo.izquierdo)
        imprimir_preorden(nodo.derecho)

# Árbol original
raiz3 = Nodo(1)
raiz3.izquierdo = Nodo(2)
raiz3.derecho = Nodo(3)
raiz3.izquierdo.izquierdo = Nodo(4)
raiz3.izquierdo.derecho = Nodo(5)

print("\n--- Challenge 3 ---")
print("Árbol original (preorden):")
imprimir_preorden(raiz3)

reflejar(raiz3)

print("\nÁrbol reflejado (preorden):")
imprimir_preorden(raiz3)
print()

# ---------------------------
# Challenge 4: Level Order Traversal
# ---------------------------

import queue

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def recorrido_por_niveles(raiz):
    """
    Retorna una lista con los valores en recorrido por niveles (BFS).
    """
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

# Árbol de ejemplo
raiz4 = NodoArbol(1)
raiz4.izquierdo = NodoArbol(2)
raiz4.derecho = NodoArbol(3)
raiz4.izquierdo.izquierdo = NodoArbol(4)
raiz4.izquierdo.derecho = NodoArbol(5)
raiz4.derecho.derecho = NodoArbol(6)

print("\n--- Challenge 4 ---")
print("Recorrido por niveles:", recorrido_por_niveles(raiz4))
print("Árbol vacío:", recorrido_por_niveles(None))
print("Árbol con un nodo:", recorrido_por_niveles(NodoArbol(99)))

# ---------------------------
# Challenge 5: Check if a Binary Tree is Balanced
# ---------------------------

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def es_balanceado(nodo):
    """
    Verifica si el árbol binario está balanceado.
    Un árbol está balanceado si para cada nodo,
    la diferencia de altura entre subárboles es como máximo 1.
    """
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

# Árbol balanceado
raiz5a = Nodo(1)
raiz5a.izq = Nodo(2)
raiz5a.der = Nodo(3)
raiz5a.izq.izq = Nodo(4)
raiz5a.izq.der = Nodo(5)

# Árbol no balanceado
raiz5b = Nodo(1)
raiz5b.izq = Nodo(2)
raiz5b.izq.izq = Nodo(3)
raiz5b.izq.izq.izq = Nodo(4)

print("\n--- Challenge 5 ---")
print("¿Árbol 1 está balanceado?", es_balanceado(raiz5a))  # True
print("¿Árbol 2 está balanceado?", es_balanceado(raiz5b))  # False
print("Árbol vacío:", es_balanceado(None))  # True
