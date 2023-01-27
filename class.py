class people:
    x=0
    y=0
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height
    def walk(self,sx,sy):
        self.x = self.x = sx
        self.y = self.y = sy
Tom = people("Tom",100,110)
print(f"start position ({Tom.x},{Tom.y})")
Tom.walk(10,154)
print(f"он на кординатах ({Tom.x},{Tom.y})")


class прямоугольник:
    def __init__(self,name,A,B):
        self.name = name
        self.A = A
        self.B = B
    def s (self):
        print(self.A*self.B)
Reptengle = прямоугольник("Reptengle", 100, 50)
print(f"прямоугольник:({Reptengle.A}*{Reptengle.B})")
