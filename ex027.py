n = input('Digite seu nome completo: ').strip().title()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n.split()[0]}.')
print(f'Seu ultimo nome é {n.split()[len(n.split())-1]}.')
