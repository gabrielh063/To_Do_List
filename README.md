# To-Do List

## Descrição

Este projeto é uma aplicação de lista de tarefas (To-Do List), construída com o framework Flask no back-end e tecnologias padrão da web (HTML, CSS e JavaScript) no front-end. O sistema permite ao usuário adicionar, editar, excluir e listar tarefas de maneira simples e eficiente, utilizando uma interface interativa.

## Estrutura do Projeto

A aplicação está organizada da seguinte forma:

```plaintext
To_Do_List/
│
├── backend/
│   ├── app.py              # Arquivo principal que contém a aplicação Flask
│   ├── models.py           # Modelos de dados, representando a estrutura do banco de dados
│   ├── routes.py           # Definição das rotas REST para as tarefas
│   └── config.py           # Configurações gerais da aplicação (como conexão com o banco)
├── frontend/
│   ├── index.html          # Página principal da aplicação
│   ├── style.css           # Estilos da aplicação
│   └── app.js              # Código JavaScript que gerencia a interação da UI
└── README.md               # Este arquivo de documentação



### Backend

- **app.py**: Inicializa a aplicação Flask e configura as rotas principais.
- **models.py**: Define os modelos de dados e interage com o banco de dados MySQL.
- **routes.py**: Gerencia as rotas da API para as operações CRUD (Criar, Ler, Atualizar, Deletar) das tarefas.
- **config.py**: Contém as configurações da aplicação, incluindo a configuração do banco de dados.

### Frontend

- **index.html**: Arquivo HTML que serve de interface para o usuário, permitindo a visualização e interação com a lista de tarefas.
- **style.css**: Arquivos de estilo que definem o layout e a aparência da interface.
- **app.js**: Scripts que manipulam eventos do usuário e interagem com a API do back-end para realizar operações nas tarefas.

## Funcionalidades

A aplicação oferece as seguintes funcionalidades:

- **Adicionar Tarefa**: Permite ao usuário adicionar uma nova tarefa à lista.
- **Visualizar Tarefas**: Exibe todas as tarefas cadastradas no sistema.
- **Editar Tarefa**: Permite ao usuário modificar as informações de uma tarefa existente.
- **Excluir Tarefa**: Permite ao usuário remover uma tarefa da lista.

## Arquitetura e Padrões

A arquitetura do projeto segue o padrão MVC (Model-View-Controller), onde:

- **Model**: A interação com o banco de dados é feita através de modelos definidos no back-end.
- **View**: O front-end exibe os dados ao usuário e recebe as interações.
- **Controller**: O Flask gerencia a lógica do servidor, tratando as rotas e interações com o banco de dados.

### Padrões Implementados

- **API RESTful**: As interações com o back-end são realizadas por meio de uma API RESTful, que permite a criação, leitura, atualização e exclusão das tarefas de forma eficiente e independente do front-end.
- **CRUD**: Operações básicas de banco de dados (Create, Read, Update, Delete) são implementadas nas rotas do Flask.

## Justificativa para a Escolha das Tecnologias

- **Flask**: Flask foi escolhido por ser um microframework leve e flexível, adequado para a criação de APIs rápidas e simples, sem a complexidade de frameworks maiores como Django.
- **MySQL**: O MySQL foi selecionado por ser um banco de dados relacional robusto, com boa integração com o Python, através da biblioteca PyMySQL.
- **JavaScript Vanilla**: A escolha do JavaScript puro para o front-end visa manter a simplicidade do projeto, sem a necessidade de bibliotecas ou frameworks adicionais como React ou Vue.js.

## Análise de Alternativas Consideradas

- **Flask vs Django**: Django foi descartado devido à sua abordagem mais "opinionated" e ao fato de que o Flask oferece maior flexibilidade e controle para esse tipo de aplicação simples.
- **MySQL vs SQLite**: Embora o SQLite seja uma opção mais simples, o MySQL foi escolhido devido à sua escalabilidade e capacidade de lidar com um maior volume de dados, sendo mais apropriado para um ambiente de produção.
- **Vanilla JavaScript vs Frameworks (React, Vue.js)**: O uso de Vanilla JavaScript foi decidido para manter o projeto simples e sem dependências adicionais, considerando que o React ou Vue.js seriam excessivos para a funcionalidade necessária.

## Diagramas UML

### Diagrama de Casos de Uso

```plaintext
+-------------------+
|     Usuário       |
+-------------------+
        |
        | (1) Visualizar Lista de Tarefas
        v
+-------------------+      +-------------------+
|   Interface Web   |----->|    API Flask      |
+-------------------+      +-------------------+
        |
        | (2) Adicionar/Excluir/Atualizar Tarefa
        v
+-------------------+
|  Banco de Dados   |
|   (MySQL)         |
+-------------------+

Diagrama de Classes

+--------------------+        +--------------------+
|     Task           |        |   Database         |
+--------------------+        +--------------------+
| - id               |        | - connection       |
| - title            |        | - cursor           |
| - description      |        +--------------------+
| - done             |                |
+--------------------+                |
       |                               |
       v                               v
+---------------------+      +-------------------+
|    TaskController   |----->|   TaskModel       |
+---------------------+      +-------------------+
| - create_task()     |      | - insert_task()    |
| - get_tasks()       |      | - update_task()    |
| - update_task()     |      | - delete_task()    |
| - delete_task()     |      +-------------------+
+---------------------+
