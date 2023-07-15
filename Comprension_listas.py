#Crea lista por cada letra de palaba "python"
lista = [letra for letra in "python"]

print (lista)

#Crea un rango entre 1 a 20 y de 2 en 2 e imprime todos los numeros que su resultado sea mayor que 10
Lista2 = [n for n in range(0,21,2) if n*2>=10]

print (Lista2)

#Crea un rango entre 1 a 20 y de 2 en 2 e imprime todos los numeros que su resultado sea mayor que 10 y muestra "no" los que no cumplres con la condición
lista3 = [n if n*2>=10 else "no" for n in range(0,21,2)]

print (lista3)

#Transforma una lista con valores en pies a otra lista en metros
pies = [10,20,30,40,50]
metros = [p * 3.281 for p in pies]

print (metros)

#Toma una lista con valores y los calcula al cuadrado
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado =[n**2 for n in valores]

#Toma una lista con valores y muestra en otro lista los valores pares
valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [n for n in valores if n%2==0]

#Toma una lista en fahrenheit y los traspasa grados celsuis en otra lista1

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]