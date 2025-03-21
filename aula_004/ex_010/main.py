file = open("aula_004/ex_010/exemplo.txt", "r", encoding="utf-8")

lines = file.readlines()
total_lines = len(lines)

if total_lines < 5:
    file = open("aula_004/ex_010/exemplo.txt", "a", encoding="utf-8")
    file.write(input("Digite algo: ") + "\n")
    file.close()
else:
    for line in lines:
        print(line.strip())

file.close()