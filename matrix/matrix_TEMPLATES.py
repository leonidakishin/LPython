import random


def print_matrix(n, a):
    """Выводит матрицу на экран, обеспечивая выравнивание столбцов."""
    width = len(str(n * n))
    for row in a:
        print(" ".join(str(x).ljust(2) for x in row))


def ij(n, a):
    """Возвращает исходную матрицу без изменений."""
    print("a[i][j]" "Исходная матрица")
    return [[a[i][j] for j in range(n)] for i in range(n)]


def ji(n, a):
    """Возвращает транспонированную матрицу."""
    print("a[j][i]", "Транспонирование матрицы")
    return [[a[j][i] for j in range(n)] for i in range(n)]  # a[j][i] = i * n + j + 1


def rotate_90_clockwise(n, a):
    """Возвращает матрицу, повернутую на 90 градусов по часовой стрелке."""
    print("a[n - j - 1][i]" "Поворот на 90 градусов по часовой стрелке")
    return [[a[n - j - 1][i] for j in range(n)] for i in range(n)]


def rotate_90_counterclockwise(n, a):
    """Возвращает матрицу, повернутую на 90 градусов против часовой стрелки."""
    print("a[j][i]" "Поворот на 90 градусов против часовой стрелки")
    return [[a[j][i] for i in range(n)] for j in range(n)]


def rotate_180(n, a):
    """Возвращает матрицу, повернутую на 180 градусов."""
    print("a[n - i - 1][n - j - 1]", "Поворот на 180 градусов")
    return [[a[n - i - 1][n - j - 1] for j in range(n)] for i in range(n)]


def rotate_270(n, a):
    """Возвращает матрицу, повернутую на 270 градусов."""
    print("a[j][n - i - 1]" "Поворот на 270 градусов")
    return [[a[j][n - i - 1] for j in range(n)] for i in range(n)]


def reflect_horizontal(n, a):
    """Возвращает матрицу, отраженную по горизонтальной оси."""
    print("Зеркальное отражение по горизонтали:")
    new_matrix = [row[:] for row in a]
    for i in range(n // 2):
        for j in range(n):
            new_matrix[i][j], new_matrix[n - i - 1][j] = (
                new_matrix[n - i - 1][j],
                new_matrix[i][j],
            )
    return new_matrix


def swap_diagonal_elements(n, a):
    """Возвращает матрицу, в которой поменяли местами элементы главной и побочной диагонали."""
    print("Поменяли местами элементы на главной и побочной диагоналях:")
    new_matrix = [row[:] for row in a]
    for i in range(n):
        new_matrix[i][i], new_matrix[n - i - 1][i] = (
            new_matrix[n - i - 1][i],
            new_matrix[i][i],
        )
    return new_matrix


def swap_columns_1_and_2(n, a):
    """Возвращает матрицу, в которой поменяли местами столбцы 1 и 2."""
    print("Поменяли местами столбцы 1 и 2:")
    new_matrix = [row[:] for row in a]
    if n > 2:
        for i in range(n):
            new_matrix[i][1], new_matrix[i][2] = new_matrix[i][2], new_matrix[i][1]
    return new_matrix


def matrix_addition(n, a, b):
    """Возвращает сумму двух матриц."""
    print("Сложение матриц: a + b")
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("Матрицы должны быть одинакового размера для сложения.")
        return None
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]


def matrix_multiplication(n, a, b):
    """Возвращает произведение двух матриц."""
    print("Умножение матриц: a * b")
    if len(a[0]) != len(b):
        print(
            "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице для умножения."
        )
        return None
    c = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c


def is_square_matrix(a):
    """Проверяет, является ли матрица квадратной."""
    rows = len(a)
    if rows == 0:
        return False
    cols = len(a[0])
    return rows == cols


def print_diagonals(n, a):
    """Выводит главную и побочную диагонали матрицы."""
    print("Главная диагональ:")
    for i in range(n):
        print(a[i][i], end=" ")
    print()

    print("Побочная диагональ:")
    for i in range(n):
        print(a[i][n - i - 1], end=" ")
    print()


def fill_matrix_random(n, min_val, max_val):
    """Заполняет матрицу случайными числами в заданном диапазоне."""
    print(f"Заполнение матрицы случайными числами от {min_val} до {max_val}:")
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]


def create_identity_matrix(n, c):
    """Создание шахматной доски."""
    print("Щахматная доска")
    new_matrix = [row[:] for row in c]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                new_matrix[i][j] = "."
            else:
                new_matrix[i][j] = "*"
    return new_matrix


def nacij(n, c):
    """Возвращает матрицу с числами на побочной диагонали равными 1, числами, стоящими ниже этой диагонали, равными 2."""
    print("a[n - i - 1][j]", "Побочная диагональ и числа ниже нее")
    new_matrix = [row[:] for row in c]
    for i in range(n):
        for j in range(n):
            if j == n - i - 1:  # Побочная диагональ
                new_matrix[i][j] = 1
            elif j < n - i - 1:  # Выше побочной диагонали
                new_matrix[i][j] = 0
            elif j > n - i - 1:  # Ниже побочной диагонали
                new_matrix[i][j] = 2
    return new_matrix


def spiral(n, c):
    """Выводит матрицу в виде спирали."""
    print("Вывод матрицы в виде спирали:")
    new_matrix = [row[:] for row in c]
    """new_matrix = [[i for i in range(row * y + 1, (row + 1) * y + 1)] for row in range(x)]
        if x == 1 or y == 1:
            return new_matrix"""
    top, bottom, left, right, num = 0, n - 1, 0, n - 1, 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            new_matrix[top][i] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            new_matrix[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left - 1, -1):
            new_matrix[bottom][i] = num
            num += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            new_matrix[i][left] = num
            num += 1
        left += 1
    return new_matrix


def plusij(n, c):
    """Возвращает матрицу, в которой элементы ниже главной диагонали равны разности индексов."""
    print("a[i][j]", "Элементы ниже главной диагонали равны разности индексов")
    new_matrix = [row[:] for row in c]
    for i in range(n):
        for j in range(n):
            if i < j:
                new_matrix[i][j] = j - i
            elif i > j:
                new_matrix[i][j] = i - j
    return new_matrix
