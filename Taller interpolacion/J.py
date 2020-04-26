from matplotlib import pyplot as pl

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
def C(n,i):
    return factorial(n)/(factorial(n-i)*factorial(i))

def Spline(n,puntos):
    coeficientesx = []
    coeficientesy = []
    for i in range(n+1):
        Coef = C(n,i)
        coeficientesx.append(Coef*puntos[i][0])
        coeficientesy.append(Coef*puntos[i][1])
    return [coeficientesx,coeficientesy]

def B(n,t,coef):
    ans = 0
    for i in range(n+1):
        ans += coef[i]*((1-t)**(n-i))*(t**i)
    return ans
       
def graficar(n,T,coeficientes):
    x = []
    y = []
    for t in T:
        x.append(B(n,t,coeficientes[0]))
        y.append(B(n,t,coeficientes[1]))
    pl.plot(x,y)
    pl.show()
    return None

T = []
for i in range(100):
    T.append(i/100.0)

puntos = [[-1.3,4],[-1.2,4],[-1,4],[-0.5,4.2],[-0.3,4.4],[-0.3,4.5],[-0.5,4.2],[-1,4.2],[-1.2,4],[-0.6,3.8],[-0.8,3.8],[-0.8,3.6],[-0.8,3.4],[-0.8,3.2],[-0.8,3],[-0.8,2.8],[-0.8,2.7],[-0.8,2.5],[-1.5,3],[-1.5,3],[-1.6,3.3],[-1.5,3.5]]
n = len(puntos)-1
coeficientes = Spline(n,puntos)
graficar(n,T,coeficientes)


