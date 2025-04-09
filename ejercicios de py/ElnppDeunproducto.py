nombre = input("Dime el nombre de tu producto: ")
precio = int(input("Dime el precio de el producto: "))
porcdescuento = int(input("Dime el porcentaje de descuento que quieres aplicar a tu producto: "))
descuento = (precio * porcdescuento)/100
print (f"El monto de tu descuento sera de: {descuento}")
total = precio - descuento
print (f"El nombre de tu producto es de {nombre}, y el precio total con el descuento aplicado es de: {total}")

