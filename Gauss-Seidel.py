def main():
    #Matriz A
    matrix = [[13, 3, 2, 1, 0, 0], 
    [3, 13, 3, 2, 1, 0],
    [2, 3, 13, 3, 2, 1],
    [1, 2, 3, 13, 3, 2],
    [0, 1, 2, 3, 13, 3],
    [0, 0, 1, 2, 3, 13]]
    #Matriz solução b
    b = [0, 0, 0, 5, 3, 5]
    #x1 guarda os valores anteriores, enquanto x2 recebe os mais recentes
    x1 = []
    x2 = []
    tam = len(matrix)
    for i in range(0, tam): #seta os valores iniciais de x1 como zero
        x1.append(0)
    while True:
        x2 = Gauss_Seidel(matrix, x1, b) #retorna os novos valores de x pelo metodo de Gauss Seidel
        if (stopping_c(x1, x2)): #caso o criterio de parada seja satisfeito retorna 'true' levando a fuga do loop
            break
        x1 = x2.copy()
    s = []
    for i in range(0, 6):
        kk = 0
        for j in range(0, 6):
            kk = kk + matrix[i][j]*x1[j] #realiza o calculo da matriz solução b, usando os valores finais de x
        s.append(kk)
    print(f'b produzido pela solução:\n {s}') #retorna a prova real
    print(f'Solução:\n{x2}') #retorna a solução da matriz x

def Gauss_Seidel(matrix, x1, b): #essa função retorna os novos valores de x
    x = x1.copy()
    tam = len(x)
    for i in range(0, tam):
        sum = 0
        for j in range(0, tam):
            if j != i: #evita que -aii*xii seja contabilizado
                sum = sum - (x[j] * matrix[i][j]) #soma todos os valores da formula: -aij*xij
        x[i] = (b[i] + sum)/matrix[i][i] #soma os valores já contabilizados ao bi e divide pelo aii
    return x

def stopping_c(x1, x2): #retorna 'True' caso o critério de parada tenha sido alcançado e 'False' caso contrário 
    tam = len(x1) 
    sum = []
    for i in range(0, tam):
        sum.append(abs(x2[i] - x1[i])) #guarda em um vetor os valores de x2i - x1i
    e = max(sum)/max(x2) #divide o maior valor do vetor anterior, pelo maior de x2
    if e <= 10**-5:
        return True
    else:
        return False

main()