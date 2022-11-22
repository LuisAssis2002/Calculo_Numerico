import numpy as np
import matplotlib.pyplot as plt

def main():
    x = [1.0, 2.0, 3.0, 4.5, 6.0, 7.5, 9.0, 10.0, 11.0]
    y = [2.0, 25, 70, 80, 220, 250, 440, 500, 560]
    x1 = np.linspace(0, 15, 20)
    y1 = Minimos_Q(x1, x, y)

    plt.plot(x1, y1)       # gráfico de linha
    plt.plot(x, y, 'o')  # gráfico com pontos
    plt.show()           # mostra o gráfico

def calc(matrix, b):
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
    for i in range(0, 2):
        kk = 0
        for j in range(0, 2):
            kk = kk + matrix[i][j]*x1[j] #realiza o calculo da matriz solução b, usando os valores finais de x
        s.append(kk)
    return x2

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

def Minimos_Q(x1, x, y):                            
    b = []
    t1t1 = len(x)
    t1t2 = sum(x)
    t2t2 = 0
    b2 = 0
    for i in x:
        t2t2 = t2t2 + i**2
    b1 = sum(y)
    for i in range(0, t1t1):
        b2 = b2 + x[i]*y[i]
    c = calc([[t1t1, t1t2], [t1t2, t2t2]], [b1, b2]) #resolve os coeficientes por Gauss-Seidel
    return c[1]*x1 + c[0]


main()
