# -----------------------------------------------------------------------------
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación - Código 213022
# Actividad: Fase 5 - Evaluación Final POA
# Problema seleccionado: 3 - Reabastecimiento de inventario
# -----------------------------------------------------------------------------

# ----------------------
# Datos iniciales (matriz de inventario)
# Formato: [Código, Nombre Artículo, Stock Actual, Stock Mínimo]
# ----------------------
inventario = [
    ["ART001", "Papel Bond Carta", 15, 50],
    ["ART002", "Tinta Negra Impresora", 8, 10],
    ["ART003", "Carpetas de Cartón", 60, 25],
    ["ART004", "Bolígrafos Azules", 22, 40],
    ["ART005", "Grapas Estándar", 5, 15],
    ["ART006", "Marcadores Permanentes", 35, 20]  # Artículo adicional
]

# ----------------------
# Módulo / Función de cálculo de pedido
# ----------------------
def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Calcula la cantidad que se debe solicitar para reabastecer un artículo
    Parámetros:
        stock_actual: Cantidad disponible en inventario
        stock_minimo: Cantidad mínima requerida
    Retorno:
        Valor entero con la cantidad exacta a pedir
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# ----------------------
# Generación del informe final
# ----------------------
print("=" * 60)
print("INFORME DE PEDIDOS DE REABASTECIMIENTO DE INVENTARIO")
print("=" * 60)
print(f"{'Nombre del Artículo':<30} | {'Cantidad a Solicitar':<25}")
print("-" * 60)

# Recorremos la matriz y aplicamos la función a cada artículo
for articulo in inventario:
    nombre = articulo[1]
    actual = articulo[2]
    minimo = articulo[3]
    
    cantidad_pedir = calcular_cantidad_pedir(actual, minimo)
    print(f"{nombre:<30} | {cantidad_pedir:<25}")

print("=" * 60)
print("Auditoría de inventario finalizada correctamente.")