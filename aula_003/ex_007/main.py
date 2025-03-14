dados_pessoais = {
    'name': 'Victor',
    'age': 22,
    'city': 'Brasília/DF',
    'work': 'Desenvolvedor'
}

print("Chaves: ")
for key in dados_pessoais.keys():
    print(f"{key}")
print("\n")

print("Valores: ")
for value in dados_pessoais.values():
    print(f"{value}")
print("\n")

print("Chaves-valores: ")
for key, value in dados_pessoais.items():
    print(f"{key}: {value}")