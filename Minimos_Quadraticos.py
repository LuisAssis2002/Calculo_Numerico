import Gauss_Seidel as gs

def Minimos_Q(x1, x, y):                            
    t1t1 = len(x)
    t1t2 = sum(x)
    t2t2 = 0
    b2 = 0
    for i in x:
        t2t2 = t2t2 + i**2
    b1 = sum(y)
    for i in range(0, t1t1):
        b2 = b2 + x[i]*y[i]
    c = gs.input([[t1t1, t1t2], [t1t2, t2t2]], [b1, b2]) #resolve os coeficientes por Gauss-Seidel
    return c[1]*x1 + c[0]



