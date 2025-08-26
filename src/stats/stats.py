class Stats:
    def promedio(self, numeros):
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        if not numeros:
            return 0
        numeros_ordenados = sorted(numeros)
        n = len(numeros_ordenados)
        mid = n // 2
        if n % 2 == 0:
            return (numeros_ordenados[mid - 1] + numeros_ordenados[mid]) / 2
        else:
            return numeros_ordenados[mid]
    
    def moda(self, numeros):
        """
        Encuentra el valor que aparece con mayor frecuencia en la lista.
        """
        if not numeros:
            return None
        frecuencia = {}
        for num in numeros:
            frecuencia[num] = frecuencia.get(num, 0) + 1
        max_frecuencia = max(frecuencia.values())
        for num in numeros:
            if frecuencia[num] == max_frecuencia:
                return num
    
    def desviacion_estandar(self, numeros):
        if not numeros:
            return 0
        mean = self.promedio(numeros)
        var = sum((x - mean) ** 2 for x in numeros) / len(numeros)
        return var ** 0.5
    
    def varianza(self, numeros):
        if not numeros:
            return 0
        mean = self.promedio(numeros)
        return sum((x - mean) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        if not numeros:
            return 
        return max(numeros) - min(numeros)
