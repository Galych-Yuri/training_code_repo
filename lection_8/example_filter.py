# У фільтр треба передавати функцію яка повертає Тру або Фолс, тобто повертає булевий результат

import random

# student_grades = list(map(range(1, 11), random.randint(55, 100)))  Функція map() приймає функцію і послідовність
# значень, до якої ця функція буде застосовуватися. У вас намагається застосувати range(1, 11) (який генерує
# послідовність від 1 до 10) до random.randint(55, 100) (який генерує випадкове число від 55 до 100).
# Для створення списку з випадковими оцінками від 55 до 100, ви не повинні використовувати map().
student_grades = [random.randint(55, 100) for _ in range(10)]
print(student_grades)


def check_grade_a(grade):
    return grade >= 75


student_grades_a = list(filter(check_grade_a, student_grades))
print(student_grades_a)  # [99, 99, 82, 81]

student_grades_a_lambda = list(filter(lambda x: x >= 75, student_grades))
print(student_grades_a_lambda)  # [99, 99, 82, 81]

 