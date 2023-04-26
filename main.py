"""
# MULTIPLOS 3 - 5
sum = 0

for i in range (1000):
    if (i % 3 == 0 or i % 5 ==0):
        sum += i

print(str(sum))
"""
"""
# Serie de Fibonacci

sum = 0
num1 = 0
num2 = 1

while num2 < 4000000:
    temp = num1
    num1 = num2
    num2 = num2 + temp
    if (num1 % 2 == 0):
        sum += num1

print (sum)
"""
"""
# El mayor factor primo

number=600851475143

primeFactor = 1
i = 2

while i <= number:
    if number % i == 0:
        primeFactor = i
        number = number / i
    else:
        i = i + 1

print(primeFactor)
"""

"""
# Palíndromo

def isPal(num):
    numString = str(num)
    for i in range(0,int(len(numString)/2+1)):
        if (numString[i] != numString[-i-1]):
            return False
    return True

maxProduct = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        result = i * j
        if isPal(result):
            if result > maxProduct:
                maxProduct = result

print(maxProduct)
"""
# Calculadora de IMC
# IMC = Peso / (Altura x Altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > de 30: obesidad



peso = int(input("Cual es tu peso en kg? \n EScribe aqui:"))
alturacent= int(input("Cual es tu altura en centimetros? \n EScribe aqui:"))
alturametros = alturacent / 100
imc = peso /(alturametros * alturametros)
print("Su IMC es: "+ str(imc))

if imc < 20:
    print (" tu peso esta por debajo de lo normal")
if imc >= 20 and imc < 26:
    print (" tu peso esta dentro  de lo normal ")
if imc >= 26 and imc < 30:
    print ("estas en sobre peso, tienes que dejar de comer fuera de casa")
if imc >=30:
    print ("tienes que emoezar a hacer deporte , dieta y visitar a tu medico")
