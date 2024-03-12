import random
import math

class Vector:

    def __init__(self, size = 3):
        
        """
        Inicjacja wektora o zadanym rozmiarze, w tym przypadku będą to
        trzy elementy o początkowej wartości 0.
        """

        self.size = size
        self. elements = [0]*size

    def generate_random(self):
        
        """
        Generuje elementy wektora i tworzy z nich listę.
        """
        
        self.elements = [random.randint(1, 100) for _ in range(self.size)]


    def __add__(self, other):
        
        """
        Dodaje dwa wektory po elementach.
        """
        
        if self.size != other.size:
            raise ValueError("Wektory nie mają tego samego rozmiaru")
        result = Vector(self.size)
        result.elements = [self.elements[i] + other.elements[i] for i in range(self.size)]
        return result

    def __sub__(self, other):
        
        """
        Odejmuje dwa wektory po elementach.
        """
        
        if self.size != other.size:
            raise ValueError("Wektory nie mają tego smego rozmiaru")
        result = Vector(self.size)
        result.elements = [self.elements[i] - other.elements[i] for i in range(self.size)]
        return result

    def __mul__(self, scalar):
        
        """
        Mnoży wektor przez skalar.
        """
        
        result = Vector(self.size)
        result.elements = [self.elements[i] * scalar for i in range(self.size)]
        return result

    def __rmul__(self, scalar):
        
        """
        Mnoży wektor przez skalar.
        """
        
        result = Vector(self.size)
        result.elements = [self.elements[i] * scalar for i in range(self.size)]
        return result

    def length(self):
        
        """
        Oblicza długość wektora
        (sumuje kwadraty wartości jego elementów i wyciąga pierwiastek).
        """
        
        return math.sqrt(sum(x**2 for x in self.elements))

    def sum(self):
        
        """
        Sumuje elementy wektora.
        """
        
        return sum(self.elements)

    def dot_product(self, other):
        
        """
        Oblicza iloczyn skalarny dwóch wektorów.
        """
        
        if self.size != other.size:
            raise ValueError("Wektory nie są tkiego samego rozmiaru")
        return sum(self.elements[i] * other.elements[i] for i in range(self.size))

    def __repr__(self):
        
        """
        Zwraca reprezentację tekstową wektora.
        """
        
        return f"Vector({self.elements})"

    def __getitem__(self, index):
        
        """
        Zwraca element o danym indeksie.
        """
        
        return self.elements[index]

    def __contains__(self, item):
        
        """
        Sprawdza czy dany element należy do wektora.
        """
        
        return item in self.elements
    
#Przykłady użycia
if __name__ == "__main__":
    v1 = Vector()
    v1.generate_random()
    print("Vector 1:", v1)

    v2 = Vector()
    v2.generate_random()
    print("Vector 2:", v2)

    v3 = v1 + v2
    print("Vector 1 + Vector 2:", v3)
    assert v3.elements == [v1.elements[i] + v2.elements[i] for i in range(v1.size)], "Addition error"

    v4 = v1 - v2
    print("Vector 1 - Vector 2:", v4)
    assert v4.elements == [v1.elements[i] - v2.elements[i] for i in range(v1.size)], "Subtraction error"

    scalar = 5
    v5 = v1 * scalar
    print("Vector 1 * Scalar:", v5)
    assert v5.elements == [v1.elements[i] * scalar for i in range(v1.size)], "Scalar multiplication error"

    print("Length of Vector 1:", v1.length())
    assert v1.length() == math.sqrt(sum([x**2 for x in v1.elements])), "Length calculation error"

    print("Sum of Vector 1:", v1.sum())
    assert v1.sum() == sum(v1.elements), "Sum calculation error"

    print("Dot Product of Vector 1 and Vector 2:", v1.dot_product(v2))
    assert v1.dot_product(v2) == sum([v1.elements[i] * v2.elements[i] for i in range(v1.size)]), "Dot product calculation error"

    print("Element at index 2 of Vector 1:", v1[2])
    assert v1[2] == v1.elements[2], "Indexing error"

    print("Is 3 in Vector 2?", 3 in v2)
    assert 3 in v2.elements, "Value check error"

