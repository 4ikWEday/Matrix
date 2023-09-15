matrix = [ [15, 2, 7, 8, 9, 10, 3, 5, 14, 11], [6, 12, 18, 4, 3, 9, 17, 11, 6, 2], [13, 5, 8, 9, 1, 20, 6, 17, 3, 14], [7, 11, 4, 16, 10, 9, 2, 14, 8, 6], [5, 3, 1, 6, 12, 7, 19, 8, 14, 15], [9, 13, 11, 15, 5, 7, 2, 6, 3, 10], [2, 7, 13, 10, 9, 8, 5, 4, 12, 1], [6, 17, 9, 4, 3, 12, 14, 5, 8, 20], [16, 5, 11, 13, 3, 9, 6, 8, 10, 1], [4, 18, 7, 9, 13, 11, 2, 3, 6, 8] ]

#Создаем 'sum' - сумма всех элементов матрицы
matrix_sum = 0
#Записываем в sum сумму чисел
for i in matrix:
    for j in i:
        matrix_sum += j

#Создаем 'max'- наибольш. элемент матрицы
matrix_max = 0
#Записываем в max наибольш. элемент
for i in matrix:
    for j in i:
        if j > matrix_max:
            matrix_max= j


#Создаем 'min' - наименьш. элемент матрицы
matrix_min = 10
#Записываем в min наимеьш. элемент
for i in matrix:
    for j in i:
        if j < matrix_min:
            matrix_min = j

#Создаем 'mode' - самый частый элемент матрицы
mode_dict = {}
for i in matrix:
    for j in i:
        mode_dict[j] = mode_dict.get(j, 0) + 1
matrix_mode = max(mode_dict, key=mode_dict.get)

print(f'Максимальный элемент матрицы - {matrix_max}')
print(f'Сумма всех элементов матрицы - {matrix_sum}')
print(f'Минимальный элемент матрицы - {matrix_min}')
print(f'Самый частый элемент матрицы - {matrix_mode}')