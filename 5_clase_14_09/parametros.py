#parametros por posicion------------------------------------------

# def calcular_precio_venta (precio_costo, porcentaje):
#     precio_venta = precio_costo * (1+porcentaje/100)
#     return precio_venta

# total = calcular_precio_venta(1000,20)
# print(f'El precio de venta es {total}')

#parametros por nombre---------------------------------------------

# def calcular_precio_venta (precio_costo, porcentaje):
#     precio_venta = precio_costo * (1+porcentaje/100)
#     return precio_venta

# total = calcular_precio_venta(porcentaje=30, precio_costo=1000)
# print(f'El precio de venta es {total}')




#parametros opcionales---------------------------------------------
def calcular_precio_venta (precio_costo:float, porcentaje:int = 20)->float:
    """
    calcula el precio de venta de un producto, aplicando el porcentaje correspondiente

    Args:
        precio_costo (float): el precio de compra del producto
        porcentaje (int, optional): porcentaje de ganancia. Defaults to 20.

    Returns:
        float: _description_
    """
    precio_venta = precio_costo * (1+porcentaje/100)
    return precio_venta

precio_venta = calcular_precio_venta(1000)

print(f'el precio de venta es {precio_venta}')