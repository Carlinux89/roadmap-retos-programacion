# tipos de operadores
# operadores aritmeticos
print("\t\t --- Programa de operadres ---\n")

num1=int(input("ingrese primer numero: "))

num2=int(input("ingrese segundo numero: "))

print("La suma es: " ,num1 + num2)
print("la resta es: ", num1 - num2)
print("la multiplicacion: ", num1 * num2)
print("la division es: ", num1 / num2)
print("la raiz cuadrada es: ", num1 ** num2)
print("el residuo es: ", num1 % num2)
print("la division entera es: ", num1 // num2)

# operadores de comparacion
print("el resultado 1==1 de: ", 1==1)
print("el resultado 1!=1 de: ",1!=1)
print("el numero mayor de 5>9 es: ",5>9)
print("el numero menor de 5<9 es: ",5<9)
print("el numero mayor o igula de 5<5 es: ",5<5)
print("el numero menor o igual de 5<9 es: ",5<9)

#operadores logicos
print("otra manera de realizar negacion not(1==1): ",not(1==1))
print("el resultado de es (1==1) and (5>9): ",(1==1) and (5>9))
print("el resultado de es (1==1) or (8!=8): ",(1==1) or (8!=8))

#operadores de asignacion
# =, +=, -=, *=, /=, %=, **=, //=
num = 11 
print(num)
num += 1
print(num)
num -= 1
print(num)
num *= 2
print(num)
num /= 2
print(num)
num %= 2
print(num)
num **= 1
print(num)
num //= 1
print(num)

# operadores de identidad
num1=1.0
print(num is num1)
num1=num
print(num is num1)
print(num is not num1)

