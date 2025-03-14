dados_pessoais = {
    'name': 'Victor',
    'age': 22,
    'city': 'Brasília/DF',
    'work': 'Desenvolvedor'
}

dados_pessoais['city'] = 'São Paulo/SP'
dados_pessoais.pop('age')

print(dados_pessoais.get('number') if dados_pessoais.get('number') else 'Chave \'Telefone\' não encontrada')