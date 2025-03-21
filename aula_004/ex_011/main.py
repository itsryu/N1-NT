file = open('aula_004/ex_011/exemplo.txt', 'w', encoding='utf-8')

added = file.write('Hello World!\n')

print(added) # 13
# O valor retornado representa a quantidade de caracteres escritos no arquivo. Nesse caso, 13 caracteres foram escritos.

file.close()