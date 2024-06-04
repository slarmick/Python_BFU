matrix = []
print("Введите элементы матрицы 3x3:")
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

for row in matrix:
    print(row)

def check_for_depend(matrix):
    det = (
            matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
            matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
            matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )
    if det != 0:
        return "Столбцы матрицы линейно независимы."
    else:
        return "Столбцы матрицы линейно зависимы."


print(check_for_depend(matrix))
