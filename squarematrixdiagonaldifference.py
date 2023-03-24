

def matrix_to_list(matrix):
    return list(map(int, matrix.rstrip().split()))


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(matrix_to_list(input()))
