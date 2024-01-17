"""
tipo numerico
"""
num = 5

# divisão com ponto flutuante
resultado = num / 2
print(resultado)

# para ter uma divisão com apenas numero inteiro
resultado = int(num / 2)
print(resultado)

# ou usando a forma pythônica
resultado = num // 2
print(resultado)

# para declarar numeros grandes podemos usar underline para separar, isso ajuda a leitura
num2 = 1_000_000
num3 = 1_000_000_000

print(num2)
print(num3)

# para descobrir o tipo podemos usar a função type

print(type(num))
print(type(resultado))

print(float(num))
