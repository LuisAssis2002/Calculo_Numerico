import numpy as np
import matplotlib.pyplot as plt
import Minimos_Quadraticos as mq

def main():
    x = [1.0, 2.0, 3.0, 4.5, 6.0, 7.5, 9.0, 10.0, 11.0]
    y = [2.0, 25, 70, 80, 220, 250, 440, 500, 560]
    x1 = np.linspace(0, 15, 20)
    y1 = mq.Minimos_Q(x1, x, y)

    plt.plot(x1, y1)     # gráfico de linha
    plt.plot(x, y, 'o')  # gráfico com pontos
    plt.show()           # mostra o gráfico

main()