from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

#url da pagina alvo

url = 'https://www.themoviedb.org/movie'    

#cabeçalho com user-agent para simular um navegador específico.
headers0 = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36' }

#fazendo a requisição com o cabeçalho e a url alvo
response = requests.get(url, headers=headers0)

#verificando se a requisição foi bem-sucedida
if response.status_code == 403:
    print(f'Erro {response.status_code}: Não autorizado')

elif response.status_code != 200:
    print(f'Erro {response.status_code}: Não foi possível acessar a página')
    #se passou daqui, tudo deu certo ao capturar a página, então vamos realizar o scrapping
else:
    #realizar o parse no conteúdo html
    soup = BeautifulSoup(response.content, 'html.parser')

    #verificar a estrutura html para ver o que está sendo retornado
    #print(soup.prettify()[:2]) #mostra as 1000 linhas do html para entender a estrutura

    #selecionando os filmes da página
    movies = soup.find_all('div', class_= 'card style_1')
    print(f'Total e filmes: {len(movies)}') #verifica quantos filmes foram encontrados

    #listar e armazenar as informações dos filmes

    movie_list = []

    #iterando sobre os filmes para extrair as informações

    for movie in movies: 
        try: 
            #extração do titulo
            title_tag = movie.find('a', class_= 'image')
            nome_filme = title_tag['title'] if title_tag else 'Título não encontrado'
            date_tag = movie.find('p')
            release_date = date_tag.get_text(strip=True) if date_tag else 'Data não encontrada'
            tabela = {'Titulo': nome_filme,'Data': release_date }
            movie_list.append(tabela)
        except Exception as travou:
            print(f'Erro ao processar o filme: {travou}')

    #convetendo os dados em um datrafram
    df = pd.DataFrame(movie_list)

    #exibir resultados
    if not df.empty:
        print(df)

        #salvar em csv
        df.to_csv('movies.csv', index=False)
        print('Tabela salva com sucesso')

        print("DAdos das datas extraidas", df['Data'].head())

        df['Data']= pd.to_datetime(df['Data'],format='%d de %b de %Y', errors='coerce')

        print("DAdos das datas extraidas", df['Data'].head())

        #extraindo o mês e ano da data
        df['Mês/Ano'] = df['Data'].dt.to_period('M')
        df['Ano'] = df['Data'].dt.to_period('Y')

        filmes_por_mes = df['Mês/Ano'].value_counts().sort_index()
        filmes_por_ano = df['Ano'].value_counts().sort_index()

        #plotar o gráfico de barras
        plt.figure(figsize=(10,6))
        filmes_por_mes.plot(kind='bar', color='skyblue')
        plt.title('Quantidade de Filmes por Mês')
        plt.xlabel('Mes/Ano')
        plt.ylabel('Quantidade de Filmes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()     
    
        #plotar gráfico de pizza
        plt.figure(figsize=(10,6))
        filmes_por_ano.plot(kind='pie', color='skyblue')
        plt.title('Quantidade de Filmes por Ano')
        plt.xlabel('Ano')
        plt.ylabel('Quantidade de Filmes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show() 

    else:
        print("Nenhum dado encontrado")

