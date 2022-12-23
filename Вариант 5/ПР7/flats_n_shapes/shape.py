class Shape:
    def __init__(self, type_of_shape, color, flat_ind):
        self.type = type_of_shape
        self.color = color
        self.flat_ind = flat_ind

    def __str__(self):
        return "Класс фигуры. Свойства: " \
               "Тип (type) str, Цвет (color) str, " \
               "Индекс плоскости (flat_ind) int"
