salario = int(input("Introduce tu salario: "))
incremento1 = (salario * 0.08)
print(f"El monto del 8 porciento dado por tu salario es de: {incremento1}")
salario2 = salario + incremento1
print (f"Tu salario con el incremento del 8 porciento es de: {salario2}")
print ("Se te debitara un 2,5 porciento de tu total: ")
descuento = salario2 * 0.025
print (f"El monto a debitar sera: {descuento}")
salario3 = salario2 - descuento
print (f"El total de tu salario es de: {salario3}")









