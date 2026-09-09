import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

def parear(precio, precio_redondo, ea, er):
    precio_par = []
    precio_r_par = []
    ea_par = []
    er_par = []
    for i in range(47):
        precio_par.append(f"{precio[i]} - {precio[i+1]}")
        precio_r_par.append(f"{precio_redondo[i]} - {precio_redondo[i+1]}")
        ea_par.append(f"{ea[i]} - {ea[i+1]}")
        er_par.append(f"{er[i]} - {er[i+1]}")
    return precio_par, precio_r_par, ea_par, er_par

def crear_csv(variaciones, precio, precio_redondo, ea, er, pro_a, pro_r):
    fechas = [elem[0] for elem in variaciones]
    precio_par, precio_r_par, ea_par, er_par = parear(precio, precio_redondo, ea, er)

    datos_combinados = np.column_stack((
    fechas,
    precio_par,
    precio_r_par,
    ea_par,
    er_par,
    pro_r,
    pro_a))
    encabezado = "Meses_Annos,Precio_Real,Precio_Aprox,Error_Absoluto,Error_Relativo,Propagacion_absoluto,Propagacion_relativo"

    np.savetxt(
    'evaluacion_errores.csv', 
    datos_combinados, 
    delimiter=',', 
    fmt='%s',
    header=encabezado, 
    comments='')
    
def grafico_serie(anno, precio, meses):
    meses_unicos = list(dict.fromkeys(meses))
    meses_corto = [f"{elem[0:3]}" for elem in meses_unicos]
    anno_unico = list(dict.fromkeys(anno))

    etiquetas_x = [f"{m} {a}" for a in anno_unico for m in meses_corto]
    x_pos = np.arange(len(etiquetas_x))

    plt.figure(figsize=(15, 6))
    plt.plot(x_pos, precio, color='red', linestyle='-', linewidth=2, marker='o')

    min_y = int(precio.min() - 20)
    max_y = int(precio.max() + 20)
    plt.ylim(min_y, max_y)

    plt.xticks(x_pos, etiquetas_x, rotation=90, fontsize=8)
    plt.ylabel('Valor Dólar (CLP)')
    plt.title('Dólar Observado SII por Mes (2022 - 2025)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("graficos/serie_mensual_dolar.png", dpi=300, bbox_inches="tight")
    plt.show()

def grafico_barras(variaciones, pro_a, precio_real=None):
    if precio_real is not None:
        delta_p = np.diff(precio_real)
    else:
        delta_p = np.array([elem[1] for elem in variaciones], dtype=float)

    etiquetas = [elem[0] for elem in variaciones]
    pro_a = np.array(pro_a, dtype=float)

    error_domina = np.abs(delta_p) <= pro_a
    colores = ["#d9534f" if e else "#337ab7" for e in error_domina]

    x = np.arange(len(delta_p))

    plt.figure(figsize=(16, 6))
    plt.bar(x, delta_p, color=colores, alpha=0.85, edgecolor="black", linewidth=0.5)
    plt.errorbar(x, delta_p, yerr=pro_a, fmt="none", ecolor="black", capsize=3, alpha=0.6)
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)

    plt.xticks(x, etiquetas, rotation=90, fontsize=8)
    plt.ylabel("$\\Delta P$")
    plt.title("$\\Delta P$ mensual — rojo: el error domina (cancelación)")

    legend_elements = [
        Patch(facecolor="#337ab7", label="$\\Delta P$ significativo"),
        Patch(facecolor="#d9534f", label="Error domina"),
    ]
    plt.legend(handles=legend_elements, loc="upper left")

    plt.grid(axis="y", linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.savefig("graficos/variacion_mensual_dolar.png", dpi=300, bbox_inches="tight")
    plt.show()

def grafico_error_representacion(anno, mes, er):
    etiquetas = [f"{m[0:3]} {a}" for a, m in zip(anno, mes)]
    x = np.arange(len(er))

    plt.figure(figsize=(15, 6))
    plt.bar(x, er, color='orange', alpha=0.7, edgecolor='black')
    plt.xticks(x, etiquetas, rotation=90, fontsize=8)
    plt.ylabel('Error Relativo (%)')
    plt.title('Gráfico 3: Error de Representación por Mes (2 Cifras Significativas)')
    plt.grid(axis='y', linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig("graficos/error_representacion.png", dpi=300, bbox_inches="tight")
    plt.show()

def grafico_rentabilidad_minimo(anno, mes, precio_redondo, ea):
    min_idx = np.argmin(precio_redondo)
    p_compra = precio_redondo[min_idx]
    ea_compra = ea[min_idx]

    precios_post = precio_redondo[min_idx:]
    ea_post = ea[min_idx:]
    etiquetas = [f"{m[0:3]} {a}" for a, m in zip(anno[min_idx:], mes[min_idx:])]

    rentabilidades = ((precios_post - p_compra) / p_compra) * 100
    er_propagado = ((ea_compra / p_compra) + (ea_post / precios_post)) * 100

    x = np.arange(len(rentabilidades))

    plt.figure(figsize=(15, 6))
    plt.errorbar(x, rentabilidades, yerr=er_propagado, fmt='-o', color='green', ecolor='black', capsize=3)
    plt.xticks(x, etiquetas, rotation=90, fontsize=8)
    plt.ylabel('Rentabilidad (%)')
    plt.title('Gráfico 4: Rentabilidad Acumulada desde el Mínimo con Error Propagado')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    plt.savefig("graficos/rentabilidad_minimo.png", dpi=300, bbox_inches="tight")
    plt.show()