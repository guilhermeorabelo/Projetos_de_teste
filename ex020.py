from random import shuffle
a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
lista = [a, b, c, d]
shuffle(lista)
print(f'A ordem de apresentação é a seguinte: {lista}')
