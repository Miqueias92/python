"""
Tipo Booleano
Algebra booleana Criada por George Boole

2 constantes, Verdadeiro e Falso

True -> Verdadeiro
False -> Falso

Obs: Sempre com inicial maiúscula

"""

ativo = True

print(ativo)

"""
Operações básicas
"""

# Negação (not)
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso
ou seja sempre negação
"""
print(not ativo)

logado = False

# Ou (Or)
"""
É uma operação binária, ou seja, depende de dois valores, Ou um ou outro deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False

"""

print(ativo or logado)

# E (and)
"""
também é uma operação binária, ou seja depende de 2 valores, ambos os valores devem ser verdadeiros

True and True -> True
False and True -> False
True and False -> False
False and False -> False
"""

