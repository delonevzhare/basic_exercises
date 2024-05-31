# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

""" students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name_counts = {}
for student in students:
    name = student['first_name']
    if name in name_counts:
        name_counts[name] += 1
    else: 
        name_counts[name] = 1
for name, count in name_counts.items():
    print(f"{name}: {count}") """
# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
""" students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_counts = {}
for student in students:
    name = student['first_name']
    if name in name_counts:
        name_counts[name] += 1
    else:
        name_counts[name] = 1
print(name_counts)

most_common_name = None
max_count = 0
for name, count in name_counts.items():
    if count > max_count:
        most_common_name = name
        max_count = count
print(f"Самое частое имя среди учеников: {most_common_name}")
# ??? """


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

class_number = 1 #Переменная для хранения текущего скласса
for class_students in school_students: #Проходимся по каждому классу в списке students
    name_counts = {} #Создаем пустой словарь для подсчета количества повторений каждого имена в класе
    for student in class_students: #Проходимася по каждому ученику в текущем классе 
        name = student['first_name'] #Извлекаем имя ученика
        if name in name_counts: #Если имя уже ексть в словаре, увеличиваем его счетчик на 1
            name_counts[name] += 1
        else: # Если имени нет в словаре, добавляем его с начальным значением 1
            name_counts[name] = 1
    
    most_common_name = None #Находим самое частое имя в текущем классе 
    max_count = 0
    for name, count in name_counts.items():
        if count > max_count:
            most_common_name = name
            max_count = count
    print(f"Самое частое имя в классе {class_number}: {most_common_name}")
    class_number += 1 #Увеличиваем класс на 1 для следующей итерации





 # ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

gender_count = {classroom['class']: {'girls': 0, 'boys': 0} for classroom in school} #Создаем словари для подсчета кол-ва девочек и мальчиков в каждом классе
for class_info in school: #Подсчитываем количество девочек и мальчиков в каждом классе
    class_name = class_info['class']
    for student in class_info['students']:
        if not is_male.get(student['first_name']):
            gender_count[class_name]['girls'] += 1
        else:
            gender_count[class_name]['boys'] += 1
for class_name, count in gender_count.items():
    print(f"Класс {class_name}: девочки {count['girls']}, мальчики {count['boys']}")


# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boys_count = {}
girls_count = {}
for school_class in school:
    class_name = school_class['class']
    boys_count[class_name] = 0
    girls_count[class_name] = 0
    for student in school_class['students']:
        if is_male[student['first_name']]: #Если ученик - мальчик
            boys_count[class_name] += 1
        else:
            girls_count[class_name] += 1

max_boys_class = max(boys_count, key=boys_count.get)
max_girls_class = max(girls_count, key=girls_count.get)

print(f'Больше всего мальчиков в классе {max_boys_class}')
print(f'Больше всего девочек в классе {max_girls_class}')



    
# ???

