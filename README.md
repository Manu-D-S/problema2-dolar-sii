# problema2-dolar-sii

**Asignatura:** Laboratorio 1 - Computación Numérica seccion 2

**Univeridad:** Universidad Católica del Maule

**Integrantes** Ariel Gallardo,Manuel Fuentes



Este laboratorio analiza el comportamiento del precio promedio mensual del dólar observado por el SII entre los meses de enero de 2022 y diciembre de 2025. El objetivo principal es evaluar cómo el uso de métodos matemáticos de precisión finita ayuda a la toma de decisiones en temas económicos; este también introduce temas de errores absolutos, relativos y propagados en operaciones de compra, venta y variación mensual de los dólares USD en precio de moneda chilena CLP, estudiando en particular el fenómeno de cancelación en números muy cercanos.

Este programa se basa en la implementación de 4 archivos de programación en Python, los cuales son:

* cargar_datos.py: Encargado de leer el archivo CSV del SII (dolar_observado_sii_2022_2025.csv) y retornar la información estructurada para procesar.  

* errores.py: Encargado de calcular los errores absolutos, errores relativos y la propagación de errores entre los datos.  

* anualidad.py: Encargado de estructurar los datos en un archivo CSV de salida (evaluacion_errores.csv) y crear los gráficos de series de tiempo, variaciones con margen de error, error de representación y rentabilidad desde el mínimo.  

* punto_flotante.py: Script principal que coordina la ejecución de todo el proyecto. Realiza las pruebas de precisión finita (comparación float32 vs float64), redondeo a cifras significativas, calcula compras, ventas, ganancias, rentabilidades, ejecuta las llamadas a los otros módulos y genera el gráfico de deriva.

Uso correcto

Para poder usar el programa de manera correcta es necesario tener instalado python y las librerias necesarias para el funcionamiento del programa los cuales son numpy y matplotlib,tambien es necesario ejecutar el programa desdes el archivo de punto_flotante.py ya que este tendra nuestro main para poder ejecutar el codigo de forma correcta.

Hallazgos y resultados relevantes

1. Mejor Estrategia segun los meses mas bajos y altos
  * Mejor mes de compra: Febrero 2023 $798.26 CLP.


  * Mejor mes de venta: Enero 2025 $1000.76 CLP.


  * Rentabilidad estimada: 25.37% de ganancia y con un margen de error de 0.29%.




2. Peor estrategia segun tramos
   
  * Los peores meses segun las variaciones son Mayo 2023 – Junio 2023 y Diciembre 2022 – Diciembre 2023 donde en estos casos el error domina la diferencia entre compra y venta.



3. Graficos
   
Se generaron dos graficos para tener una referencia visual de la informacion procesada:

  * serie_mensual_dolar.png: Muestra de manera visual los valores que toma el dólar a lo largo de los meses evaluados.
    
  * variacion_mensual_dolar.png: Muestra la variación entre meses en formato de barras, donde el color azul indica que la variación le ganó al error, mientras que las barras rojas significan que los              errores son mayores que la variación.
  
  * error_representacion.png: Representa el porcentaje de error relativo introducido al truncar o redondear los precios a cifras significativas mes a mes.
  
  * rentabilidad_minimo.png: Muestra la curva de rentabilidad acumulada comprando en el punto mínimo (Febrero 2023) y vendiendo en cada mes posterior, incluyendo barras de error propagado.
  
  * deriva_ida_vuelta.png: Visualiza las diferencias en pesos CLP producidas por el ciclo de conversión de monedas en aritmética de punto flotante.  
