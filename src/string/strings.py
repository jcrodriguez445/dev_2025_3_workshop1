class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """

    def es_palindromo(self, texto):
        texto = texto.replace(" ", "").lower()
        return texto == texto[::-1]

    def invertir_cadena(self, texto):
        invertida = ""
        for i in range(len(texto) - 1, -1, -1):
            invertida += texto[i]
        return invertida

    def contar_vocales(self, texto):
        vocales = "aeiouAEIOU"
        contador = 0
        for c in texto:
            if c in vocales:
                contador += 1
        return contador

    def contar_consonantes(self, texto):
        contador = 0
        for c in texto:
            if c.isalpha() and c.lower() not in "aeiou":
                contador += 1
        return contador

    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())

    def contar_palabras(self, texto):
        return len(texto.split())

    def palabras_mayus(self, texto):
        resultado = ""
        i = 0
        while i < len(texto):
            if texto[i].isspace():
                resultado += texto[i]
                i += 1
            else:
                resultado += texto[i].upper()
                i += 1
                while i < len(texto) and not texto[i].isspace():
                    resultado += texto[i]
                    i += 1
        return resultado

    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        espacio_anterior = False
        for c in texto:
            if c == " ":
                if not espacio_anterior:
                    resultado += c
                    espacio_anterior = True
            else:
                resultado += c
                espacio_anterior = False
        return resultado

    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] in "+-":
            texto = texto[1:]
        if not texto:
            return False
        for c in texto:
            if c < "0" or c > "9":
                return False
        return True

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []  # Caso especial: subcadena vacía
        posiciones = []
        n = len(texto)
        m = len(subcadena)
        for i in range(n - m + 1):
            coincidencia = True
            for j in range(m):
                if texto[i + j] != subcadena[j]:
                    coincidencia = False
                    break
            if coincidencia:
                posiciones.append(i)
        return posiciones
