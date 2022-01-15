#Diseñar un programa que dados una serie de 15 números pueda devolver:
#el mayor, el menor, la suma y el promedio de todos los números.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
menor= 0
mayor = 0
suma = 0
promedio = 0
print("El mayor de los números de la lista es: " + str(max(lista)))
print("El menor de los números de la lista es: " + str(min(lista)))
for numero in lista:
    suma= suma + numero 
print ("La suma de todos los números es: " + str(suma))
promedio = suma / len(lista)
print ("El promedio de los números es : " + str(promedio))
print("Los números utilizados en este ejercicio fueron " + str(lista))

    
    

