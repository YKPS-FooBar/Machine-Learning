#Tensors

class Vector:

    def __init__(self,array):
        self.array=array

    def __add__(self,vec):
        if type(vec)==Vector:
            array=vec.array
            if len(self.array)!=len(array):
                raise ValueError('Arrays must be the same length')
            for i in range(0,len(array)):
                self.array[i]+=array[i]
        else:
            for i in range(0,len(self.array)):
                self.array[i]+=vec
        return Vector(self.array)
                
    def __sub__(self,vec):
        if type(vec)==Vector:
            array=vec.array
            if len(self.array)!=len(array):
                raise ValueError('Arrays must be the same length')
            for i in range(0,len(array)):
                self.array[i]-=array[i]
        else:
            for i in range(0,len(self.array)):
                self.array[i]-=vec
        return Vector(self.array)

    def __mul__(self,vec):
        if type(vec)==Vector:
            array=vec.array
            if len(self.array)!=len(array):
                    raise ValueError('Arrays must be the same length')
            out=0
            for i in range(0,len(array)):
                    out+=self.array[i]*array[i]
            return out
        else:
            for i in range(0,len(self.array)):
                self.array[i]*=scale
            return Vector(self.array)
