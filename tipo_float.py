"""
 tipo float
 separador é ponto e não virgula
"""

# forma errada, do ponto de vista de declaração de um float
# pois está usando virgula (,), e não ponto, mas gera uma tupla
num1 = 1, 4
print(num1)

# forma correta
num1 = 2.2
print(num1)
print(type(num1))

# é possivel fazer dupla atribuição

n1, n2 = 1, 44

print(n1)
print(n2)


# podemos converter float para int
n3 = 4.4
res = int(n3)
print(res)

# podemos trabalhar com números complexos
print("trabalhando com números complexos")

numero2 = 5j
print(numero2)
