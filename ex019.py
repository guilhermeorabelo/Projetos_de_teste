import random
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
lista = [a, b, c, d]
print(f'O aluno escolhido foi {random.choice(lista)}.')
