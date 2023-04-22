class Figure:
    unit = "cm"

    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return 3.14 * (self.__radius ** 2)

    def info(self):
        print(f"Circle radius: {self.__radius}{self.unit}, area: {self.calculate_area():.2f}{self.unit}.")


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        self.__side_a = side_a
        self.__side_b = side_b

    def calculate_area(self):
        return (self.__side_a * self.__side_b) / 2

    def info(self):
        print(f"RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit}, area: {self.calculate_area():.2f}{self.unit}.")


circle1 = Circle(5)
circle2 = Circle(7)

triangle1 = RightTriangle(3, 4)
triangle2 = RightTriangle(5, 12)
triangle3 = RightTriangle(8, 15)


figures = [circle1, circle2, triangle1, triangle2, triangle3]


for figure in figures:
    figure.info()
