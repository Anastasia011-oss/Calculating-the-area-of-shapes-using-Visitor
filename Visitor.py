from abc import ABC, abstractmethod


class Visitor(ABC):

    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

    @abstractmethod
    def visit_triangle(self, triangle):
        pass

    @abstractmethod
    def visit_compound_shape(self, compound):
        pass


class AreaVisitor(Visitor):

    def visit_circle(self, circle):
        area = 3.14 * circle.radius ** 2
        print(f"Площадь круга: {area}")
        return area

    def visit_rectangle(self, rectangle):
        area = rectangle.width * rectangle.height
        print(f"Площадь прямоугольника: {area}")
        return area

    def visit_triangle(self, triangle):
        area = 0.5 * triangle.base * triangle.height
        print(f"Площадь треугольника: {area}")
        return area

    def visit_compound_shape(self, compound):
        total = 0
        for shape in compound.children:
            total += shape.accept(self)
        print(f"Общая площадь группы: {total}")
        return total


class Shape(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: Visitor):
        return visitor.visit_circle(self)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor: Visitor):
        return visitor.visit_rectangle(self)


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def accept(self, visitor: Visitor):
        return visitor.visit_triangle(self)


class CompoundShape(Shape):

    def __init__(self):
        self.children = []

    def add(self, shape: Shape):
        self.children.append(shape)

    def accept(self, visitor: Visitor):
        return visitor.visit_compound_shape(self)


class Application:

    @staticmethod
    def run():
        shapes = CompoundShape()
        shapes.add(Circle(3))
        shapes.add(Rectangle(4, 5))
        shapes.add(Triangle(6, 2))

        visitor = AreaVisitor()
        shapes.accept(visitor)


if __name__ == "__main__":
    Application.run()