# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
name = {}
for student in students:
    name_student = student['first_name']
    if name_student in name:
        name[name_student]+=1
    else:
        name[name_student]=1
for man in name:
    print(man, name[man])


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name = {}
for student in students:
    name_student = student["first_name"]
    if name_student in name:
        name[name_student]+=1
    else:
        name[name_student]=1
most_name = max(name, key=name.get)
print(f'Самое часто повторяющееся имя: {most_name}')


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
def most_name(names):
    name_count = {}
    for name in names:
        if name in name_count:
            name_count[name] +=1
        else:
            name_count[name] = 1
    return max(name_count, key=name_count.get)

for class_index, students in enumerate(school_students, start=1):
    name = [student['first_name'] for student in students]
    most_full_name = most_name(name)
    print(f'Самое часто повторяющееся имя в классе {class_index}: {most_full_name}')


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

class_stats = {}

for class_info in school:
    clase_name = class_info['class']
    students = class_info['students']

    girls_count = 0
    boys_count = 0

    for student in students:
        first_name = student['first_name']

        if is_male[first_name]:
            boys_count += 1
        else:
            girls_count += 1

    class_stats[clase_name] = (girls_count, boys_count)

# Выводим результаты
for class_name, (girls_count, boys_count) in class_stats.items():
    print(f'Класс {class_name}: девочки {girls_count}, мальчики {boys_count}')

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

max_boys_count = 0
max_boys_class = None
max_girls_count = 0
max_girls_class = None

for class_info in school:
    class_names = class_info['class']
    students = class_info['students']

    girls_count = 0
    boys_count = 0

    for student in students:
        first_name = student['first_name']

        if is_male[first_name]:
            boys_count += 1
        else:
            girls_count +=1
    
    if boys_count > max_boys_count:
        max_boys_class = boys_count
        max_boys_class = class_names

    if girls_count > max_girls_count:
        max_girls_count = girls_count
        max_girls_class = class_names

if max_boys_class:
    print(f'Больше всего мальчиков в классе {max_boys_class}')
if max_girls_class:
    print(f'Больше всего девочек в классе {max_girls_class}')
