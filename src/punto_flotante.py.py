import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import abrir_csv
from errores import errores
from anualidad import (crear_csv, grafico_serie, grafico_barras, grafico_error_representacion, grafico_rentabilidad_minimo)

def redondear(precio):
    magnitud = np.floor(np.log10(np.abs(precio)))
    factor = 10 ** (1 - magnitud)
    return np.round(precio * factor) / factor

def comprar(m, precio_redondo, mes):
    min = np.argmin(precio_redondo)
    mejor_mes = mes[min]
    usd = m / precio_redondo[min]
    return usd, mejor_mes

def vender(usd, precio_redondo, mes):
    max = np.argmax(precio_redondo)
    mejor_mes = mes[max]
    plata = usd * precio_redondo[max]
    return plata, mejor_mes

def ganancia(m, plata):
    return plata - m

def rentabilidad(g, m):
    return str(int(g/m *100))+'%'

def variacion(meses, precio_redondo, anno):
    variaciones = []
    for i in range (len(meses)-1):
        temp = []
        temp.append(f"{anno[i]} - {meses[i]} - {meses[i+1]}")
        temp.append(int(precio_redondo[i+1] - precio_redondo[i]))
        variaciones.append(temp)
    return variaciones

def pruebas_punto_flotante():
    v1_64, v2_64 = np.float64(874.67), np.float64(875.66)
    v1_32, v2_32 = np.float32(874.67), np.float32(875.66)
    print("Diferencia float64:", v2_64 - v1_64)
    print("Diferencia float32:", v2_32 - v1_32)

def grafico_deriva_ida_vuelta(anno, mes, precio):
    monto_inicial = 1000000.0
    derivas = []
    for p in precio:
        usd = monto_inicial / p
        monto_final = usd * p
        derivas.append(monto_final - monto_inicial)

    etiquetas = [f"{m[0:3]} {a}" for a, m in zip(anno, mes)]
    x = np.arange(len(derivas))

    plt.figure(figsize=(15, 6))
    plt.plot(x, derivas, color='purple', marker='s', linestyle='--')
    plt.axhline(0, color='black', linewidth=0.8, linestyle=':')
    plt.xticks(x, etiquetas, rotation=90, fontsize=8)
    plt.ylabel('Diferencia (CLP)')
    plt.title('Gráfico 5: Deriva de la Ida y Vuelta en Punto Flotante (B2)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig("graficos/deriva_ida_vuelta.png", dpi=300, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    monto = 1000000
    anno, mes, precio = abrir_csv()
    precio_redondo = redondear(precio)
    ea, er, pro_a, pro_r = errores(precio, precio_redondo)
    usd, mejor_mes_compra = comprar(monto, precio_redondo, mes)
    plata, mejor_mes_venta = vender(usd, precio_redondo, mes)
    total = ganancia(monto, plata)
    rent = rentabilidad(total, monto)
    variaciones = variacion(mes, precio_redondo, anno)
    pruebas_punto_flotante()
    crear_csv(variaciones, precio, precio_redondo, ea, er, pro_a, pro_r)
    grafico_serie(anno, precio_redondo, mes)                       
    grafico_barras(variaciones, pro_a, precio)                      
    grafico_error_representacion(anno, mes, er)                     
    grafico_rentabilidad_minimo(anno, mes, precio_redondo, ea)     
    grafico_deriva_ida_vuelta(anno, mes, precio)                    