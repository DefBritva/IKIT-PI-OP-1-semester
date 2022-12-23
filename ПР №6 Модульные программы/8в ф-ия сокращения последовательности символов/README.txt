Гопиенко Александр
КИ22-17/2Б

8 Вариант
Пакет package

1) Модуль shortline.py

	Содержит функции shortened_line и line_classic
	Функции содержат доктесты

	stortened_line - функция сокращения строки
	:param classic_line: строка, которую нужно преобразовать в сокращённый вид
	:return result: сокращённая строка
	Пример: aaabbb
	-> a3b3
	
	line_classic - функция преобразования сокращённой строки в обычную
	:param short_line: сокращённая строка, которую нужно преобразовать
    	:return back_line: строка без сокращений
    	Пример: a5bcde4
    	-> Строка без сокращений -  aaaaabcdeeee

2) Модуль workalg.py
	
	Содержит функции check_digits, digit_begin, digit_zero
	Функции содержат доктесты
	
	check_digits - проверка строки, если она полностью состоит из цифр
	:param check_line: строка для проверки
    	:return all(check_list): True/False
    	для проверки условия в функции main()
    	Пример: 228
    	-> Вы ввели числа!
	
	digit_begin - проверка на строку, если она начинается с цифры
	:param begin_line: строка для проверки
    	:return True: True,
     	если строка начинается с цифры
    	Пример: 1soft
    	-> Строка начинается с цифры
	
	digit_zero - проверка на строку, если в ней содержатся нули
	:param zero_line: строка для проверки
    	:return True: True,
    	если строка содержит 0
    	Пример: compucter0
    	-> Строка начинается с цифры

3) Модуль tests.py
	
	Принимает модули workalg, shortline
	
	Провододимые тесты:
	
	test_empty - тест на пустую строчку
	test_line_classic - тест работы функции line_classic
	test_shortened_line - тест работы функции shortened_line 
	test_check_digits - тест работы функции check_digits
	test_digit_begin - тест работы функции digit_begin
	test_digit_zero - тест работы функции digit_zero

4) Модуль __main__.py
	
	Принимает модули shortline, workalg, tests, argparse, pytest, doctest
	Содержит точку входа функция
	
	Пример: a3b5
    	-> Строка без сокращений - aaabbbbb

5) Модуль инициализации пакета __init__.py
	
	