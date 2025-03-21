with open('aula_004/ex_012/exemplo.txt', 'w', encoding='utf-8') as file:
    file.write('Hello World!\n')

with open('aula_004/ex_012/exemplo.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        print(line.strip())