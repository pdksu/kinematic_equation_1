import numpy as np

def j1(x):
    # Safe evaluation to avoid division by zero
    x = np.asarray(x)
    with np.errstate(divide='ignore', invalid='ignore'):
        result = np.where(x == 0, 0.0, (np.sin(x)/x**2 - np.cos(x)/x))
    return result


def j2(x):
    x = np.asarray(x)
    with np.errstate(divide='ignore', invalid='ignore'):
        term1 = (3 / x**3 - 1 / x) * np.sin(x)
        term2 = -3 * np.cos(x) / x**2
        result = np.where(x == 0, 0.0, term1 + term2)
    return result

def chebyshev_Tn(n, x):
    x = np.asarray(x)
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return x
    Tn_1 = x
    Tn_2 = np.ones_like(x)
    for _ in range(2, n + 1):
        Tn = 2 * x * Tn_1 - Tn_2
        Tn_2, Tn_1 = Tn_1, Tn
    return Tn

def legendre_Pn(n, x):
    x = np.asarray(x)
    if n == 0:
        return np.ones_like(x)
    elif n == 1:
        return x
    Pn_2 = np.ones_like(x)
    Pn_1 = x
    for k in range(2, n + 1):
        Pn = ((2*k - 1)*x*Pn_1 - (k - 1)*Pn_2) / k
        Pn_2, Pn_1 = Pn_1, Pn
    return Pn

def runge_like(x):
    return 1 / (1 + 25 * x**2)

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    x = np.linspace(-1, 9, 1000)
    y1 = j1(x)
    y2 = j2(x)
    y1 = runge_like(x)
    y1 = legendre_Pn(3, np.sin(x))
    y2 = legendre_Pn(4, np.sin(x))
    c12 = y1*y2
    plt.plot(x, y1,'-r', label='j1(x)')
    plt.plot(x, y2,'-b', label='j2(x)')
    # plt.plot(x, c12, '-g', label='j1(x) * j2(x)')
    plt.xlabel('x')
    plt.ylabel('j1(x)')     
    plt.show()