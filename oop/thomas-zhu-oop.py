# This document is made on the maxim:
# NEVER REINVENT THE WHEEL

# I entered this on GitHub so I haven't tested this

# Create a vector class
class Vector:
    """It's a vector. What more do you expect?"""

    def __init__(self, numbers):
        self._numbers = [float(n) for n in numbers]
    
    def __iter__(self):
        return iter(self._numbers)
    
    def __len__(self):
        return len(self._numbers)
    
    def __getitem__(self, key):
        return self._numbers[key]
    
    def __setitem__(self, key, value):
        self._numbers[key] = value
    
    def __delitem__(self, key):
        del self._numbers[key]
    
    def __contains__(self, value):
        return value in self._numbers
    
    def __pos__(self):
        # Why would someone call this?
        return self
    
    def __neg__(self):
        return Vector(-i for i in self)

    def __abs__(self):
        return sum(i ** 2 for i in self) ** (1/2)
    
    def __add__(self, vector):
        vector = Vector(vector)
        assert len(self) == len(vector)
        return Vector((i + j for i, j in zip(self, vector)))
    
    def __sub__(self, vector):
        return self + (-Vector(vector))
    
    def __mul__(self, vector):
        vector = Vector(vector)
        assert len(self) == len(vector)
        return Vector((i * j for i, j in zip(self, vector)))
    
    def __floordiv__(self, vector):
        vector = Vector(vector)
        assert len(self) == len(vector)
        return Vector((i // j for i, j in zip(self, vector)))
    
    def __div__(self, vector):
        vector = Vector(vector)
        assert len(self) == len(vector)
        return Vector((i / j for i, j in zip(self, vector)))
    
    def __mod__(self, vector):
        vector = Vector(vector)
        assert len(self) == len(vector)
        return Vector((i % j for i, j in zip(self, vector)))
    
    def __pow__(self, power, mod=None):
        return Vector(pow(i, power, mod) for i in self)
