# Bring Back Coffee Shop

![home-intro](readme_prints/banner.PNG)

<h3 align="center">
    E-commerce de uma cafeteria vintage com Python/Flask
</h3>

> [Vídeo completo mostrando o site]()

# Sumário

* [INTRODUÇÃO](#bring-back-coffee-shop)
* [SUMÁRIO](#sumário)
* [TECNOLOGIAS](#tecnologias)
  * [PRÉ-REQUISITOS](#pré-requisitos)
* [FUNCIONALIDADES](#funcionalidades)
* [TELAS DO SITE - PREVIEWS](#telas-do-site)
  * [HOMEPAGE](#homepage)
  * [LOGIN E CADASTRO](#login-e-cadastro)
  * [PRODUTOS](#produtos)
  * [CARRINHO](#carrinho)
  * [LOGOUT](#logout)
  * [ADMIN](#admin)
* [Entre em contato!](#entre-em-contato)

# Tecnologias

Nesse projeto foram usadas as seguintes tecnologias:
- [Python](https://www.python.org)
- [Flask Microframework](https://flask.palletsprojects.com/en/2.1.x/)
  - [Flask WTForms](https://flask-wtf.readthedocs.io/en/1.0.x/)
  - [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
  - [Flask User](https://flask-user.readthedocs.io/en/latest/)
  - [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

### Pré-requisitos
Para ver todos, consulte o requirements.txt, ou faça a instalação pelo comando:
```console
$ pip install -r requirements.txt
```

Se quiser instalar separadamente:

Instalando Flask, Flask SqlAlchemy, Flask Migrate, Flask WTForms, Flask User
```console
$ pip install Flask
$ pip install -U Flask-SQLAlchemy
$ pip install Flask-Migrate
$ pip install -U Flask-WTF
$ pip install Flask-User
```

Inicialização do Banco de Dados 
```console
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade
$ flask db --help
```

# Funcionalidades
Features do projeto:
- Login e Cadastro com banco de dados
- Vista geral de todos os produtos
- Vista individual de um produto
- Escolher a quantidade do produto para por no carrinho
- Carrinho
- Separação por categorias que são especificadas na hora do cadastro do produto
- Filtragem por ordem alfabética, por preço crescente e por preço decrescente
- Área para o administrador ter um fácil acesso à adição, edição, exclusão e leitura (dashboard) dos produtos

# Telas do Site

[Link pro Template base](https://freemiumdownload.com/downloads/e-shopper-free-ecommerce-html-template/)
## Homepage
![home-intro](readme_prints/banner.PNG)

---

## Login e Cadastro

![login-register](readme_prints/login-register.gif)

---

## Produtos

### Todos os Produtos

![produtos](readme_prints/produtos.gif)

### Produto Individual

![produto_individual](readme_prints/produto_individual.gif)

### Categorias e Filtros

![categorias_filtros](readme_prints/categorias_filtros.gif)

---

## Carrinho

![carrinho](readme_prints/carrinho.gif)

---

## Admin
Área para os administradores/donos do e-commerce poderem gerenciar os produtos facilmente

### Dashboard
![admin_dashboard](readme_prints/admin_dashboard.gif)

### Adicionar Protudo
![admin_add_produto](readme_prints/admin_add_produto.PNG)

---

# Entre em contato!

> [Linkedin](https://www.linkedin.com/in/beatriz-vidal-a2b114200) | [Instagram](https://www.instagram.com/bvidalf/) | [E-mail](mailto:biavidalf@gmail.com) 👋
>
> Made by Beatriz Vidal ❤🎯