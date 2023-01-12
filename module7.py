import matplotlib.pyplot as plt

def fact(n):
    if n == 0:
        return [1]
    else:
        L = [1]
        return L.append()

def fact2(n):
    if n == 0:
        return 1
    else:
        factoriel = [1]
        terme = 1
        for i in range(1,n+1):
            terme = terme*i
            factoriel.append(terme)
        return factoriel