from Calculadora import Calculadora

calular = Calculadora()

num1 = int(input('Ingrese el número 1 :'))
num2 = int(input('Ingrese el número 2 :'))




calular.numero1= num1
calular.numero2= num2

suma = calular.suma(calular.numero1, calular.numero2)

print(suma)