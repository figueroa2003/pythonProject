# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento y el monto final de una compra.

    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
    descuento (float): El monto del descuento.
    monto_final (float): El monto final después de aplicar el descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

# Llamada a la función con el descuento predeterminado del 10%
monto_total_1 = 100
descuento_1, monto_final_1 = calcular_descuento(monto_total_1)
print(f"Monto total: ${monto_total_1}, Descuento: ${descuento_1}, Monto final: ${monto_final_1}")

# Llamada a la función especificando un porcentaje de descuento diferente
monto_total_2 = 200
descuento_2, monto_final_2 = calcular_descuento(monto_total_2, 15)
print(f"Monto total: ${monto_total_2}, Descuento: ${descuento_2}, Monto final: ${monto_final_2}")
