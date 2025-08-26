class Logica:
    """
    Clase con métodos para realizar operaciones de lógica booleana y algoritmos.
    """
    
    def AND(self, a, b):
        return a and b
    
    def OR(self, a, b):
        return a or b
    
    def NOT(self, a):
        return not a
    
    def XOR(self, a, b):
        return (a and not b) or (not a and b)
    
    def NAND(self, a, b):
        return not (a and b)
    
    def NOR(self, a, b):
        return not (a or b)
    
    def XNOR(self, a, b):
        return not ((a and not b) or (not a and b))
    
    def implicacion(self, a, b):
        """
        La implicación a -> b es falsa solo cuando a es True y b es False.
        """
        return (not a) or b
    
    def bi_implicacion(self, a, b):
        """
        La bi-implicación a <-> b es verdadera cuando ambos valores son iguales.
        """
        return a == b

    
    
