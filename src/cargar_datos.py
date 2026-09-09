import numpy as np

def abrir_csv():
    datos = np.genfromtxt('dolar_observado_sii_2022_2025.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')
    anno = []
    mes = []
    precio = []
    for elem in datos:
        anno.append(int(elem[0]))
        mes.append(str(elem[1]))
        precio.append(float(elem[3]))
    precio_final = np.array(precio)
    return anno, mes, precio_final