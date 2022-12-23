class Flat:
    def __init__(self, size, shapes=None):
        if shapes is None:
            shapes = []
        self.shapes = [*shapes]
        self.size = size

    def add_shape(self, shape_ind):
        self.shapes.append(shape_ind)

    def __str__(self):
        return "Класс плоскости. Свойства: " \
               "Размер (size) int[x, y], Индексы фигур (shapes) int[]"
