import pandas as pd
import random 
from datetime import datetime, timedelta

# função para gerar dados de vendas ficticios

def gerar_dados(num_linhas, in_min, in_max):
    produtos = ['Tupperware', 'Brombril', 'Xerox','Kodak']
    cidades = ['Orlando', 'Anahein', 'Franco da Rocha', 'Poa']
    dados = []
    #in_min = 0
    #in_max = 365
    for _ in range(num_linhas):
        produto = random.choice(produtos)
        cidade = random.choice(cidades)
        valor = round(random.uniform(50,500),2)
        data = datetime.today() - timedelta(days=random.randint(in_min,in_max))
        dados.append([produto,cidade,valor,data])
    return dados

#gerar 100 linhas de dados com intervalo de datas de 1 a 365 dais
dados_prontos = gerar_dados(100, 1, 365)

#criar o dataframe (efetivamenta a tabela)
df_vendas = pd.DataFrame(dados_prontos,columns=['produto','cidade','valor','data'])

#salvando em csv
df_vendas.to_excel('vendas.xlsx' , index=False , engine='openpyxl')

print("Deu tudo certo! O arquivo foi saldo!")




