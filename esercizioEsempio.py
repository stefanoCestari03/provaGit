class Circulo:
    def __init__(self, radio=None, color=None):
        if radio is None:
            self.radio = 5
        else:
            self.radio = radio

        if color is None:
            self.color = "rojo"
        else:
            self.color = color

        self.area = self.calcular_area()

    def calcular_area(self):
        return 3.14159 * (self.radio ** 2)