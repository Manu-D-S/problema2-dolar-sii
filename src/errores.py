import numpy as np

def sumar(lista):
    res = []
    for i in range(len(lista)-1):
        res.append(round(lista[i] + lista[i+1], 2))
    return res

def errores(precio, precio_redondo):
    absoluto = np.round(np.abs(precio - precio_redondo), 2)
    relativo = np.round((absoluto / precio) * 100, 2)
    pro_a = sumar(absoluto)
    pro_r = sumar(relativo)
    return absoluto, relativo, pro_a, pro_r