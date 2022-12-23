flag = True

while flag:
    text = input("Введите текст: ")
    # text = """Принимая во внимание показатели успешности, реализация намеченных плановых заданий предоставляет
    # широкие возможности для модели развития. Внезапно, элементы политического процесса, которые представляют собой
    # яркий пример континентально-европейского типа политической культуры, будут призваны к ответу. В частности,
    # укрепление и развитие внутренней структуры позволяет выполнить важные задания по разработке существующих
    # финансовых и административных условий. Также как граница обучения кадров обеспечивает широкому кругу
    # (специалистов) участие в формировании экспериментов, поражающих по своей масштабности и грандиозности.
    # Современные технологии достигли такого уровня, что внедрение современных методик обеспечивает широкому кругу
    # (специалистов) участие в формировании существующих финансовых и административных условий. Ясность нашей позиции
    # очевидна: базовый вектор развития предоставляет широкие возможности для позиций, занимаемых участниками в
    # отношении поставленных задач."""

    if len(text) == 0:
        print("Длина текста должна быть больше 0!")
        flag = False
        continue

    text.lower()
    list_of_symbols = [".", ",", "(", ")", "\n", "-"]
    for i in list_of_symbols:
        text = text.replace(i, " ")

    arr = text.split(" ")
    arr = [i for i in arr if i != ""]
    if not len(arr):
        print("Длина текста должна быть больше 0!")
        continue
    arr = [i.lower() for i in arr if bool(i)]

    length = len(arr)

    unique_arr = set(arr)
    length_unique = len(unique_arr)

    dict_of_counts = {}
    for i in unique_arr:
        dict_of_counts[i] = 0
    for i in arr:
        dict_of_counts[i] += 1

    sorted_arr = sorted(list(dict_of_counts.items()), key=lambda i: i[1])
    sorted_arr = [list(i) for i in sorted_arr]
    min_count = min(dict_of_counts.values())
    max_count = max(dict_of_counts.values())
    rarest_words = []
    most_frequent_words = []
    for i in sorted_arr:
        if min_count == max_count:
            rarest_words.append(i[0])
            most_frequent_words.append(i[0])
        elif i[1] == min_count:
            rarest_words.append(i[0])
        elif i[1] == max_count:
            most_frequent_words.append(i[0])

    arr_of_lengths = [len(i) for i in arr]
    summ = sum(arr_of_lengths)
    average_len = summ / len(arr_of_lengths)

    print(f"Длина текста: {length}\nКоличество уникальных слов: {length_unique}\n"
          f"Самые редкие слова: {rarest_words}\nСамые частые слова: {most_frequent_words}\n"
          f"Средняя длина слова: {average_len}")

    if not input("Хотите запустить алгоритм заново? (y / n) ") == "y":
        break
