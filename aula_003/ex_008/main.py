data = {
    '12345678900': 'Fulano de Tal',
    '98765432100': 'Beltrano de Tal',
    '45612378900': 'Ciclano de Tal',
    '78945612300': 'Deltrano de Tal',
    '32165498700': 'Eltano de Tal'
}

input_cpf = input('Digite o CPF: ')

if data.get(input_cpf):
    print('Nome:', data[input_cpf])
else:
    print('CPF não encontrado')