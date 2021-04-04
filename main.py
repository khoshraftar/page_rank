from smaple_data import *


def matrix_multiplication(matrix1, matrix2, n):
    result = [[0 for x in range(n)] for y in range(n)]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


precision_index = 50
res = graph1
for _ in range(50):
    res = matrix_multiplication(graph1, res, 5)

# check convergence
res2 = matrix_multiplication(graph1, res, 5)
diff = 0
for i in range(len(res2)):
    for j in range(len(res2[i])):
        diff = diff + (res2[i][j] - res[i][j])
print("diff is:", diff)

for i in res:
    for j in i:
        print("%.4f" % j, end=" ")
    print()

print("page ranks:")
for i in range(len(res[0])):
    print(i, ":", res[0][i])
