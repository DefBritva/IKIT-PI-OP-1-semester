from shape import Shape


class Polygon(Shape):
    def __init__(self, type_of_shape, color, flat_ind, vertices):
        super().__init__(type_of_shape, color, flat_ind)
        self.vertices = [*vertices]

    def __str__(self):
        return "Класс многоугольника. Наследован от класса фигуры. " \
               "Свойства (помимо родительских):\n" \
               "Вершины (vertices) int[][]"
