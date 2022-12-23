from pick import pick
from tkinter import *
import re
import json
import os
from shapes import Circle, Triangle, Square, Rectangle
from flat import Flat
TYPES = ["circle", "triangle", "square", "rectangle"]
TYPES_RUS = ["Круг", "Треугольник", "Прямоугольник", "Квадрат"]
COEFFICIENT = 15

FLATS = []
SHAPES = []


def get_inp(title, type_of_inp, mx=50, default=""):
    """
    Получение и валидация ввода от пользователя в различных
    форматах (числа, строки, координаты)
    :return: int | str | tuple[int, int]
    """
    match type_of_inp:
        case "int":
            try:
                cand = int(input(title))
            except ValueError:
                print("Введено не число, попробуйте ещё раз.")
                return get_inp(title, "int")
            if 0 < cand <= mx:
                return cand
            else:
                print(f"Введено не число > 0 или указано слишком "
                      f"большое число (максимум для этого значения "
                      f"- {mx}), попробуйте ещё раз.")
                return get_inp(title, "int")
        case "color":
            inp = input(title).replace("#", "")
            if inp == "" and default != "":
                return default
            if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', "#" + inp):
                return "#" + inp
            else:
                print("Введен не цвет, попробуйте ещё раз.")
                return get_inp(title, "color")
        case "coords":
            inp = input(title).split(",")
            if len(inp) != 2:
                print("Введено некорретное значение, попробуйте ещё раз.")
                return get_inp(title, "coords")
            try:
                x, y = [int(i) for i in inp]
            except ValueError:
                print("Введены не числа, попробуйте ещё раз.")
                return get_inp(title, "coords")
            if len([i for i in (x, y) if 0 < i <= mx]) == 2:
                return int(x), int(y)
            else:
                print(f"Введены не числа > 0 или указаны слишком "
                      f"большие числа (максимум для этого значения "
                      f"- {mx}), попробуйте ещё раз.")
                return get_inp(title, "coords")
        case "text":
            inp = input(title)
            if len(inp) < 1:
                print("Введена пустая строка, попробуйте ещё раз.")
                return get_inp(title, "text")
            else:
                return inp


def get_flat():
    """
    Получение индекса плоскости от пользователя
    :return: ind: int
    """
    arr = [f"Плоскость {i}. Размер: {'x'.join([str(x) for x in val.size])}"
           for i, val in enumerate(FLATS)]
    _, ind = pick(arr,
                  title="Выберите плоскость для фигуры: ",
                  indicator="=>")
    return ind


def create_shape():
    """
    Создание новой фигуры
    """
    if not len(FLATS):
        print("В данный момент не создано ни одной плоскости; "
              "Фигура может существовать только на плоскости")
        return
    _, ind = pick(TYPES_RUS,
                  title="Выберите тип создаваемой фигуры: ",
                  indicator="=>")
    match ind:
        case 0:
            rad, center, color = \
                get_inp("Введите радиус: ",
                        "int"), \
                    get_inp("Введите координаты центра в формате x,y: ",
                            "coords"), \
                    get_inp("Введите цвет фигуры в формате #000000: ",
                            "color")
            shape = Circle(color, len(FLATS) - 1, center, rad)
            flat = FLATS[get_flat()]
            if center[0] - rad < 0 or center[1] - rad < 0 \
                    or center[0] + rad > flat.size[0] \
                    or center[1] + rad > flat.size[1]:
                print("Круг с такими параметрами не поместится "
                      "на данной плоскости")
                del shape
                return
            SHAPES.append(shape)
            flat.add_shape(len(SHAPES) - 1)
        case 1:
            ver1, ver2, ver3, color = \
                get_inp("Введите координаты первой вершины в формате x,y: ",
                        "coords"), \
                    get_inp("Введите координаты второй вершины "
                            "в формате x,y: ", "coords"), \
                    get_inp("Введите координаты третьей вершины "
                            "в формате x,y: ", "coords"), \
                    get_inp("Введите цвет фигуры в формате #000000: ",
                            "color")
            shape = Triangle(color, len(FLATS) - 1, (ver1, ver2, ver3))
            flat = FLATS[get_flat()]
            if len([i for i in (ver1, ver2, ver3)
                    if i[0] <= flat.size[0] and i[1] <= flat.size[1]]) != 3:
                print("Треугольник с такими вершинами не поместится "
                      "на данную плоскость")
                del shape
                return
            SHAPES.append(shape)
            flat.add_shape(len(SHAPES) - 1)
        case 2:
            start, w, h, color = \
                get_inp("Введите координаты начальной точки в формате x,y: ",
                        "coords"), \
                    get_inp("Введите ширину (x): ", "int"), \
                    get_inp("Введите высоту (y): ", "int"), \
                    get_inp("Введите цвет фигуры в формате #000000: ",
                            "color")
            flat = FLATS[get_flat()]
            shape = Rectangle(color, len(FLATS) - 1,
                              ((start[0], start[1]),
                               (start[0], start[1] + h),
                               (start[0] + w, start[1] + h),
                               (start[0] + w, start[1])))
            if len([i for i in shape.vertices
                    if i[0] <= flat.size[0] and i[1] <= flat.size[1]]) != 4:
                print("Прямоугольник с такими вершинами не поместится "
                      "на данную плоскость")
                del shape
                return
            SHAPES.append(shape)
            flat.add_shape(len(SHAPES) - 1)
        case 3:
            start, w, color = \
                get_inp("Введите координаты начальной точки в формате x,y: ",
                        "coords"), \
                    get_inp("Введите длину стороны: ", "int"), \
                    get_inp("Введите цвет фигуры в формате #000000: ",
                            "color")
            shape = Square(color, len(FLATS) - 1,
                           ((start[0], start[1]),
                            (start[0], start[1] + w),
                            (start[0] + w, start[1] + w),
                            (start[0] + w, start[1])))
            flat = FLATS[get_flat()]
            if len([i for i in shape.vertices
                    if i[0] <= flat.size[0] and i[1] <= flat.size[1]]) != 4:
                print("Квадрат с такими вершинами не поместится "
                      "на данную плоскость")
                del shape
                return
            SHAPES.append(shape)
            flat.add_shape(len(SHAPES) - 1)
    print(f"Фигура {len(SHAPES) - 1} успешно создана!")


def create_flat():
    l, w = get_inp("Плоскость будет начинаться в 0,0 и будет длиной,шириной: ",
                   "coords")
    flat = Flat((l, w))
    FLATS.append(flat)
    print(f"Плоскость {len(FLATS) - 1} успешно создана!")


def print_shapes():
    if len(SHAPES) == 0:
        print("Фигур нет")
    for i, v in enumerate(SHAPES):
        print(f"""--------------
Фигура {i}

Тип: {TYPES_RUS[TYPES.index(v.type)]}
Цвет: #{v.color.replace("#", "")}
Площадь: {round(v.get_area(), 3)}
Принадлежит плоскости с индексом: {v.flat_ind}
--------------""")


def print_flats():
    if len(FLATS) == 0:
        print("Плоскостей нет")
    for i, v in enumerate(FLATS):
        print(f"""--------------
Плоскость {i}

Размеры: {v.size[0]}x{v.size[1]}
Количество фигур: {len(v.shapes)}
--------------""")


def visualize():
    """
    Визуализация плоскости с помощью tkinter
    """
    flat_ind = get_flat()
    flat = FLATS[flat_ind]
    bg = get_inp("Введите цвет заднего фона в формате [#ffffff]: ",
                 "color", default="#ffffff")
    w, h = flat.size[0] * COEFFICIENT, flat.size[1] * COEFFICIENT
    tk = Tk()
    tk.title(f"Плоскость {FLATS.index(flat)}. "
             f"Размер: {'x'.join([str(x) for x in flat.size])}")
    canvas = Canvas(tk, height=h, width=w, bg=bg)
    for i in flat.shapes:
        shape = SHAPES[i]
        match shape.type:
            case "triangle":
                ver1, ver2, ver3 = \
                    (shape.vertices[0][0] * COEFFICIENT,
                     shape.vertices[0][1] * COEFFICIENT), \
                        (shape.vertices[1][0] * COEFFICIENT,
                         shape.vertices[1][1] * COEFFICIENT), \
                        (shape.vertices[2][0] * COEFFICIENT,
                         shape.vertices[2][1] * COEFFICIENT)
                canvas.create_polygon(ver1[0], ver1[1], ver2[0], ver2[1],
                                      ver3[0], ver3[1], fill=shape.color, outline="")
            case "circle":
                x0, y0, x1, y1 = (shape.center[0] - shape.rad) * COEFFICIENT, \
                                 (shape.center[1] - shape.rad) * COEFFICIENT, \
                                 (shape.center[0] + shape.rad) * COEFFICIENT, \
                                 (shape.center[1] + shape.rad) * COEFFICIENT
                canvas.create_oval(x0, y0, x1, y1, fill=shape.color, outline="")

            case _:
                x0, y0, x1, y1 = shape.vertices[0][0] * COEFFICIENT, \
                                 shape.vertices[0][1] * COEFFICIENT, \
                                 shape.vertices[2][0] * COEFFICIENT, \
                                 shape.vertices[2][1] * COEFFICIENT
                canvas.create_rectangle(x0, y0, x1, y1, fill=shape.color, outline="")

    canvas.pack()
    tk.mainloop()


def save():
    """
    Загрузка данных из json
    """
    name = get_inp("Введите название конфигурации: ", "text")
    cur_data = {
        "flats": [i.__dict__ for i in FLATS],
        "shapes": [i.__dict__ for i in SHAPES]
    }
    with open("flats_n_shapes/data.json", "r") as f:
        data = json.loads(f.read())
        data[name] = cur_data
    with open("flats_n_shapes/data.json", "w") as f:
        f.write(json.dumps(data))
    print("Сохранение файлов прошло успешно!")


def load():
    """
    Загрузка данных в json
    """
    with open("flats_n_shapes/data.json", "r") as f:

        data = json.loads(f.read())
        _, ind = pick(list(data.keys()),
                      title="Выберите название конфигурации, "
                            "из которой хотите загрузить данные",
                      indicator="=>"
                      )
        for i, v in enumerate(data[list(data.keys())[ind]]["flats"]):
            FLATS.insert(i, Flat(v["size"], v["shapes"]))
        for i in data[list(data.keys())[ind]]["shapes"]:
            match i["type"]:
                case "circle":
                    SHAPES.append(Circle(i["color"], i["flat_ind"],
                                         i["center"], i["rad"]))
                case "triangle":
                    SHAPES.append(Triangle(i["color"], i["flat_ind"],
                                           i["vertices"]))
                case "rectangle":
                    SHAPES.append(Rectangle(i["color"], i["flat_ind"],
                                            i["vertices"]))
                case "square":
                    SHAPES.append(Square(i["color"], i["flat_ind"],
                                         i["vertices"]))

        print("Загрузка данных прошла успешно!")


def main():
    while True:
        _, ind = pick(
            ["Создать новую фигуру", "Создать новую плоскость",
             "Просмотреть все фигуры", "Просмотреть все плоскости",
             "Визуализировать плоскость",
             "Сохранить текущие фигуры и плоскости в файл",
             "Загрузить фигуры и плоскости из файла",
             "Очистить консоль", "Выйти"],
            title="Добро пожаловать в программу "
                  "для вских нехороших штук с фигурами). "
                  "Выберите команду:",
            indicator="=>")
        match ind:
            case 0:
                create_shape()
            case 1:
                create_flat()
            case 2:
                print_shapes()
            case 3:
                print_flats()
            case 4:
                visualize()
            case 5:
                save()
            case 6:
                load()
            case 7:
                os.system("cls")
            case 8:
                exit()
        cmd = input("Продолжить работу с программой? ([y] / n) ")
        if not cmd == "y" and not cmd == "":
            break


if __name__ == "__main__":
    main()
