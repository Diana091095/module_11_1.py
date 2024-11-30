# numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.

import numpy as np
from random import randint


vec1 = np.array([8,9,3])
vec2 = np.array([6,26,32])

# сумма векторов
sum_vec = vec1 + vec2
print(sum_vec)

# произведение вектора на число
multiplication = 7 * vec1
print(multiplication)

# сколярное произведение
work = np.dot(vec1, vec2)
print(work)

#модуль вектора(норма вектора)
module_ = np.linalg.norm(vec1)
print(module_)

#создание рандомного вектора и определение единичного вектора рандомного вектора
vec3 = np.array([randint(1, 40), randint(47, 98), randint(5, 7)])
modul_vec3 = np.linalg.norm(vec3)
unit_vec3 = vec3 / modul_vec3
modul_unit_vec3 = np.linalg.norm(unit_vec3)
print(modul_unit_vec3)