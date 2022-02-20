f = input('Digite uma frase: ').strip()
print(f'A letra A aparece {f.upper().count("A")} vezes.')
print(f'A primeira letra A aparece na posição {1+f.upper().find("A")}')
print(f'A ultima letra A aparece na posição {1+f.upper().rfind("A")}')
