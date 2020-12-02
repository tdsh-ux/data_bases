# O que está no menu? 

Este repositório contém os notebooks e os scripts para a avaliação da disciplina de Banco de Dados, ministrada remotamente na Escola de Matemática Aplicada pelo professor Renato Souza. 

Dando continuação ao trabalho iniciado [neste repositório](https://github.com/tdsh-ux/dataBases) (em que podem ser encontradas as descrições das bases de dados e como inseri-las em um servidor MySQL através do Python; os scripts, no entanto, para ler os dados estão [nesta pasta](https://github.com/tdsh-ux/data_bases/tree/main/RScriptsCleaning); para inseri-los no servidor local do SQL, use [este notebook](https://github.com/tdsh-ux/data_bases/blob/main/dumpScript.ipynb)), buscamos, aqui, gerar e fazer o deploy de uma aplicação contendo uma visualização em grafo do banco de dados. 

Inicialmente, lemos os dados do servidor do MySQL; em seguida, determinamos a frequência com que cada par de pratos aparece em um menu e geramos a tabela para o grafo. Os detalhes estão [neste notebook](https://github.com/tdsh-ux/data_bases/blob/main/read_data.ipynb). 

Então, utilizamos o Dash para a aplicação Web. Usufruimos, por um lado, dos Dash Core Components e dos Dash HTML Components para os gráficos e para o layout geral do aplicativo; por outro, utilizamos JavaScript para a visualização dos nós e das arestas; os detalhes estão [neste notebook](https://github.com/tdsh-ux/data_bases/blob/main/app.ipynb). A imagem ilustra o deploy da aplicação, deliberadamente intitulado `the-db-food-app-strikes-back`, que está disponível [aqui](https://the-db-food-app-strikes-back.herokuapp.com/). 

<p align="center"> 
  <img src="https://github.com/tdsh-ux/data_bases/blob/main/images/app.png" width="100%" title="Heroku Application"> 
</p> 

# Diretórios

📦data_bases\
 ┣ 📂data_csv\
 ┃ ┣ 📜nodes_year_1851.0.csv\
 ┃ ┣ 📜nodes_year_1857.0.csv\
 ┃ ┣ 📜nodes_year_1862.0.csv\
 ┃ ┣ 📜nodes_year_1866.0.csv\
 ┃ ┣ 📜nodes_year_1873.0.csv\
 ┃ ┣ 📜nodes_year_1880.0.csv\
 ┃ ┣ 📜nodes_year_1881.0.csv\
 ┃ ┣ 📜nodes_year_1882.0.csv\
 ┃ ┣ 📜nodes_year_1883.0.csv\
 ┃ ┣ 📜nodes_year_1884.0.csv\
 ┃ ┣ 📜nodes_year_1888.0.csv\
 ┃ ┣ 📜nodes_year_1891.0.csv\
 ┃ ┣ 📜nodes_year_1893.0.csv\
 ┃ ┣ 📜nodes_year_1895.0.csv\
 ┃ ┣ 📜nodes_year_1898.0.csv\
 ┃ ┣ 📜nodes_year_1899.0.csv\
 ┃ ┣ 📜nodes_year_1900.0.csv\
 ┃ ┣ 📜nodes_year_1901.0.csv\
 ┃ ┣ 📜nodes_year_1905.0.csv\
 ┃ ┣ 📜nodes_year_1906.0.csv\
 ┃ ┣ 📜nodes_year_1913.0.csv\
 ┃ ┣ 📜nodes_year_1914.0.csv\
 ┃ ┣ 📜nodes_year_1917.0.csv\
 ┃ ┣ 📜nodes_year_1918.0.csv\
 ┃ ┣ 📜nodes_year_1940.0.csv\
 ┃ ┣ 📜nodes_year_1941.0.csv\
 ┃ ┣ 📜nodes_year_1948.0.csv\
 ┃ ┣ 📜scatter_data.csv\
 ┃ ┗ 📜table.csv\
 ┣ 📂dump\
 ┃ ┣ 📜currency.sql\
 ┃ ┣ 📜dish.sql\
 ┃ ┣ 📜event.sql\
 ┃ ┣ 📜menu.sql\
 ┃ ┣ 📜menu_item.sql\
 ┃ ┣ 📜menu_page.sql\
 ┃ ┣ 📜schemaTables.sql\
 ┃ ┣ 📜sponsor.sql\
 ┃ ┗ 📜venue.sql\
 ┣ 📂images\
 ┃ ┗ 📜app.png\
 ┣ 📂RScriptsCleaning\
 ┃ ┣ 📜dishScript.R\
 ┃ ┣ 📜menuScript.R\
 ┃ ┗ 📜tables.R\
 ┣ 📜.gitignore\
 ┣ 📜app.ipynb\
 ┣ 📜app.py\
 ┣ 📜dumpScript.ipynb\
 ┣ 📜food.json\
 ┣ 📜README.md\
 ┗ 📜read_data.ipynb\
