class Data:
    """
    Clase con métodos para operaciones y manipulaciones de estructuras de datos.
    Incluye implementaciones y algoritmos para arreglos, listas y otras estructuras.
    """
    
    def invertir_lista(self, lista):
        """
        Invierte el orden de los elementos en una lista sin usar reversed() o lista[::-1].
        """
        resultado = []
        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])
        return resultado
    
    def buscar_elemento(self, lista, elemento):
        """
        Busca un elemento en una lista y devuelve su índice (o -1 si no existe).
        """
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
    
    def eliminar_duplicados(self, lista):
        """
        Elimina elementos duplicados de una lista sin usar set().
        Mantiene el orden original de aparición.
        Duplicado = mismo valor y mismo tipo (1 y True NO se consideran iguales).
        """
        resultado = []
        for elem in lista:
            ya_esta = False
            for x in resultado:
                if x == elem and type(x) is type(elem):
                    ya_esta = True
                    break
            if not ya_esta:
                resultado.append(elem)
        return resultado
    
    def merge_ordenado(self, lista1, lista2):
        """
        Combina dos listas ordenadas en una sola lista ordenada.
        """
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
        resultado.extend(lista1[i:])
        resultado.extend(lista2[j:])
        return resultado
    
    def rotar_lista(self, lista, k):
        """
        Rota los elementos de una lista k posiciones a la derecha.
        """
        n = len(lista)
        if n == 0:
            return []
        k = k % n
        return lista[-k:] + lista[:-k]
    
    def encuentra_numero_faltante(self, lista):
        """
        Encuentra el número faltante en una lista de enteros del 1 al n.
        """
        n = len(lista) + 1
        suma_esperada = n * (n + 1) // 2
        suma_real = sum(lista)
        return suma_esperada - suma_real
    
    def es_subconjunto(self, conjunto1, conjunto2):
        """
        Verifica si conjunto1 es subconjunto de conjunto2 sin usar set.
        """
        for elem in conjunto1:
            encontrado = False
            for x in conjunto2:
                if elem == x:
                    encontrado = True
                    break
            if not encontrado:
                return False
        return True
    
    def implementar_pila(self):
        """
        Implementa una estructura de datos tipo pila (stack) usando listas.
        """
        pila = []
        
        def push(x):
            pila.append(x)
        
        def pop():
            if pila:
                return pila.pop()
            return None
        
        def peek():
            if pila:
                return pila[-1]
            return None
        
        def is_empty():
            return len(pila) == 0
        
        return {"push": push, "pop": pop, "peek": peek, "is_empty": is_empty}
    
    def implementar_cola(self):
        """
        Implementa una estructura de datos tipo cola (queue) usando listas.
        """
        cola = []
        
        def enqueue(x):
            cola.append(x)
        
        def dequeue():
            if cola:
                return cola.pop(0)
            return None
        
        def peek():
            if cola:
                return cola[0]
            return None
        
        def is_empty():
            return len(cola) == 0
        
        return {"enqueue": enqueue, "dequeue": dequeue, "peek": peek, "is_empty": is_empty}
    
    def matriz_transpuesta(self, matriz):
        """
        Calcula la transpuesta de una matriz.
        """
        if not matriz:
            return []
        filas = len(matriz)
        columnas = len(matriz[0])
        transpuesta = []
        for j in range(columnas):
            nueva_fila = []
            for i in range(filas):
                nueva_fila.append(matriz[i][j])
            transpuesta.append(nueva_fila)
        return transpuesta
