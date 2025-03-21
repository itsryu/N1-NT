file = open("aula_004/ex_009/exemplo.txt", "r", encoding="utf-8")

lines = file.readlines()
total_lines = len(lines)

for line in lines:
    print(line.strip())

file.close()
