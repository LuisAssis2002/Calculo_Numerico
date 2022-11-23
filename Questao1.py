import Gauss_Seidel as gs

#Matriz A
matrix = [[13, 3, 2, 1, 0, 0], 
    [3, 13, 3, 2, 1, 0],
    [2, 3, 13, 3, 2, 1],
    [1, 2, 3, 13, 3, 2],
    [0, 1, 2, 3, 13, 3],
    [0, 0, 1, 2, 3, 13]]
#Matriz solução b
b = [0, -2.25, 0, 5, -20, 3.1415]
x = gs.input(matrix, b)
print(x)