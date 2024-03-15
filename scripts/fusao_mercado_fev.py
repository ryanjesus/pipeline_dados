from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'

# Extract
print('-=-'*20)
dados_empresaA = Dados.leitura_dados(path_json, 'json')
print(f'Nome coluna Empresa A: {dados_empresaA.nome_colunas}')
print(f'Numeros de linhas Empresa A: {dados_empresaA.qtd_linha}')

print('-=-'*20)
dados_empresaB = Dados.leitura_dados(path_csv, 'csv')
print(f'Nome coluna Empresa B: {dados_empresaB.nome_colunas}')
print(f'Numeros de linhas Empresa B: {dados_empresaB.qtd_linha}')

# Transform

key_mapping = {'Nome do Item': 'Nome do Produto',
                'Classificação do Produto': 'Categoria do Produto',
                'Valor em Reais (R$)': 'Preço do Produto (R$)',
                'Quantidade em Estoque': 'Quantidade em Estoque',
                'Nome da Loja': 'Filial',
                'Data da Venda': 'Data da Venda'}

print('-=-'*20)
dados_empresaB.rename_columns(key_mapping)
print(f'Nome colunas atualizadas: {dados_empresaB.nome_colunas}')

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)

print('-=-'*20)
print(f'Nome coluna: {dados_fusao.nome_colunas}')
print(f'Numeros de linhas: {dados_fusao.qtd_linha}')

# load
print('-=-'*20)
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)

print(f'Salvando os dados... {path_dados_combinados}')
