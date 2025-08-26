class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal, etc.
    """

    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        fib_seq = []
        a, b = 0, 1
        for _ in range(n):
            fib_seq.append(a)
            a, b = b, a + b
        return fib_seq

    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n

    def triangulo_pascal(self, filas):
        triangulo = []
        for i in range(filas):
            fila = [1]
            if triangulo:
                ultima_fila = triangulo[-1]
                fila.extend([ultima_fila[j] + ultima_fila[j + 1] for j in range(len(ultima_fila) - 1)])
                fila.append(1)
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(abs(n))
        potencia = len(digitos)
        return sum(int(d) ** potencia for d in digitos) == n

    def es_cuadrado_magico(self, matriz):
        if not matriz or len(matriz) != len(matriz[0]):
            return False
        n = len(matriz)
        suma_objetivo = sum(matriz[0])
        
        # Revisar filas
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False
        # Revisar columnas
        for col in range(n):
            if sum(matriz[row][col] for row in range(n)) != suma_objetivo:
                return False
        # Revisar diagonales
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False
        return 
