# O que está no menu?

Este repositório contém os notebooks e os scripts para a avaliação da disciplina de Banco de Dados, ministrada remotamente na Escola de Matemática Aplicada pelo professor Renato Souza.

Dando continuação ao trabalho iniciado [neste repositório](https://github.com/tdsh-ux/dataBases) (em que podem ser encontradas as descrições das bases de dados e como inseri-las em um servidor MySQL através do Python; os scripts, no entanto, para ler os dados estão [nesta pasta](https://github.com/tdsh-ux/data_bases/tree/main/RScriptsCleaning); para inseri-los no servidor local do SQL, use [este notebook](https://github.com/tdsh-ux/data_bases/blob/main/dumpScript.ipynb), buscamos, aqui, gerar e fazer o deploy de uma aplicação contendo uma visualização em grafo do banco de dados, cujo modelo físico está na figura seguinte. 

<p align="center">
  <img src="https://github.com/tdsh-ux/data_bases/blob/main/images/physicalModel.jpeg" width="100%" title="Physical Model">
</p>

Inicialmente, lemos os dados do servidor do MySQL; em seguida, determinamos a frequência com que cada par de pratos aparece em um menu e geramos a tabela para o grafo. Os detalhes estão [neste notebook](https://github.com/tdsh-ux/data_bases/blob/main/read_data.ipynb).

Então, utilizamos o Dash para a aplicação Web. Usufruimos, por um lado, dos Dash Core Components e dos Dash HTML Components para os gráficos e para o layout geral do aplicativo; por outro, utilizamos JavaScript para a visualização dos nós e das arestas; os detalhes estão [neste notebook](https://github.com/tdsh-ux/data_bases/blob/main/app.ipynb). A imagem ilustra o deploy da aplicação, deliberadamente intitulado `the-db-food-app-strikes-back`, que está disponível [aqui](https://the-db-food-app-strikes-back.herokuapp.com/).

<p align="center">
  <img src="https://github.com/tdsh-ux/data_bases/blob/main/images/app.png" width="100%" title="Heroku Application">
</p>

## Guia de dump no server local
1. Execute o script SQL [schemaTables.sql](https://github.com/tdsh-ux/data_bases/blob/main/dump/schemaTables.sql) para criar o esquema de tabelas.
2. Execute algumas células do notebook [dumpScript.ipynb](https://github.com/tdsh-ux/data_bases/blob/main/dumpScript.ipynb) para popular as tabelas. (No notebook há instruções a respeito de quais células executar)

Pronto! Agora você possui os dados em seu Banco MySql.

## Descrição dos Dados
Alguns pratos são ubíquos: resistem ao tempo e são indiferentes ao espaço. Ovos mexidos são um acompanhamento presente em praticamente qualquer restaurante; usualmente é acompanhado de ovos com baicon, embora, às vezes, se oferça baicon com ovos; estes acompanhamentos, no entanto, são disjuntos. Em adição, alguns alimentos usuais, como água, apresentam nomes com pomposidade em situações peculiares: temos a água imperial; a água de congresso, parceira perene do uísque escocês; e a água de Hathorn, com sua vizinhança de pratos franceses. Além disso, a salada italiana é vendida com a batata francesa e o Stilton inglês; os cardápios transcendem fronteiras, e a globalização é perpétua.

Em uma época sem McDonalds e sem Burger King, hambúrgueres não compunham as refeições principais dos indivíduos (hoje o fazem!); contudo, temos, em nossos cardápios, a [hamburg chicken](https://en.wikipedia.org/wiki/Hamburg_chicken) é oferecida com tomate seco e com Consommê frio. Ora, a despeito disso, os hoje vetustos cidadãos podiam desfrutar das miríficas batatas fritas; no lugar do irresistível sanduíche, entretanto, havia omelete (e ovos mexidos!). Para os fissurados em açúcar, havia também o que comer: os tarteletes de maçã, geralmente servidos com azeitonas secas e com conhaque, estão no menu; torta de amora, acompanhada de nozes inglesas, também; para os clientes de paladar extravagante, tapioca de pêssego constava como alternativa.

E o que temos no menu? Entre restaurantes americanos que servem batatas francesas com acompanhamentos italianos; tortas doces acompanhadas de conhaque; e ovos com baicons e baicon com ovos, os hábitos alimentares são resilientes ao relógio. Cardápios não são influenciados por guerras, muros ou pandemias; ovos mexidos e pratos preenchidos com nomes pomposos ainda permeimam nossos catálogos. É isso que temos no menu.

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
 ┃ ┣ 📜app.png\
 ┃ ┗ 📜physicalModel.jpeg\
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
