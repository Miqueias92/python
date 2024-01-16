# pegando dados do usuário

# ---------------  usar print e input -------------------
print("Qual seu nome: ")
name = input()

print("Qual sua idade: ")
age = input()

# ----------------- usar apenas o input ----------------
# outra forma de pegar dados do usuário
sobrenome = input("qual seu sobrenome? ")
print(sobrenome)

# saída de dados
print("Olá", name, "seja bem vindo(a)")
print("O(a) %s tem %s anos" % (name, age))

# Exemplo de print 'antigo' 2.x
# print("Seja bem vindo(a) %s" % name)
# print("O(a) %s tem %s anos" % (name, age))

# Exemplo de print 'novo'
# print("Seja bem vindo(a) {0}".format(name))
# print("O(a) {0} tem {1} anos".format(name, age))

print("O(a) {0} tem {1} anos".format(name, age))

# Exemplo de print mais atual > 3.7
# print(f'Seja bem vindo(a) {name}')
print(f'Seja bem vindo (a) {name} sua idade é {age}')


