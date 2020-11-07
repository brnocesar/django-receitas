# django-receitas

0. [Rodando a aplicação](#0-rodando-a-aplicação)  
1. [Preparando o ambiente virtual](#1-preparando-o-ambiente-virtual)  
2. [Criando o projeto](#2-criando-o-projeto)  
3. [Apps](#3-apps)  
  3.1. Criando um app  
  3.2. Registrando um app  
  3.3. Primeira rota  
4. [Arquivos estáticos](#4-arquivos-estáticos)  
  4.1. Definindo arquivos estáticos no HTML  
  4.2. Criando uma nova _view_  
  4.3. Extendendo código HTML e _patials_  
  4.4. Apresentando informações de forma dinâmica  
5. [Banco de Dados](#5-banco-de-dados)  
6. [_Models_ e _migrations_](#6-_models_-e-_migrations_)  
7. [Django Admin](#7-django-admin)  
8. [Recuperando dados do Banco e apresentando nas _views_](#8-recuperando-dados-do-banco)  
  8.1 Listando as receitas  
  8.2 Detalhes de uma receita  

## 0 Rodando a aplicação

Execute os comandos abaixo na raiz do diretório clonado:

1. Criar ambiente virtual: `python3 -m venv ./venv`
2. Carregar ambiente virtual: `source $(pwd)/venv/bin/activate`
3. Instalar dependências (certifique-se que o ambiente virtual está ativado): `pip install -r requirements.txt`
4. Carregar arquivos estáticos: `python manage.py collectstatic`
5. Criar uma base de dados no PostgreSQL e adicionar as credênciais de acesso na váriavel `DATABASES` em `djangoreceitas/settings.py`
6. Rodar as _migrations_: `python manage.py migrate`
7. Criar um _super user_ para o Django Admin: `python manage.py createsuperuser`
8. Subir o servidor local: `python manage.py runserver`

## 1 Preparando o ambiente virtual

- Instalação do pacote no sistema:

```terminal
apt-get install python3-venv
```

- Criação do ambiente dentro da pasta que vai ficar a aplicação:

```terminal
mkdir django-receitas
cd django-receitas
python3 -m venv ./venv
```

- Carregando o ambiente: `source <full path>/django-receitas/venv/bin/activate`

```terminal
source <full path>/django-receitas/venv/bin/activate
```

ou, na raiz do diretório da aplicação:

```terminal
source $(pwd)/venv/bin/activate
```

- Instalação do Django **no ambiente virtual**:
  
```terminal
pip install django
```

- Verificando módulos instalados no ambiente virtual:
  
```terminal
pip freeze
```

[↑ voltar ao topo](#django-receitas)

## 2 Criando o projeto

- Lista de comandos disponíveis na cli do Django:

```terminal
django-admin help
```

- Criando o projeto da aplicação (_commit_ [938745e](https://github.com/brnocesar/alura/commit/938745e0a1f78395e8be1b5e88af6b2fcd47de6a)):

```terminal
django-admin startproject djangoreicetas .
```

- Subindo o servidor:

```terminal
python manage.py runserver
```

[↑ voltar ao topo](#django-receitas)

## 3 Apps

Os Apps do Django podem ser entendidos como "sub-aplicações" (?) com a finalidade de representar domínios (?) da aplicação. Ou da pra dizer que é a entidade mesmo? Um projeto é uma coleção de configurações e apps que formam um _site_; e um app é uma "sub-aplicação" com uma finalidade/responsabilidade (única?) bem definida, podendo fazer parte de vários projetos.

### 3.1 Criando um app

Criando um app na raiz da aplicação:

```terminal
python manage.py startapp receitas
```

Para criar o app dentro de uma pasta dedicada, primeiro devemos criar essa pasta e então podemos passar como segundo parâmetro o caminho onde o app deverá ser criado (_commit_ [60f0ad1](https://github.com/brnocesar/alura/commit/60f0ad14ef51e6229afb3b0ad0738d0db721cf64)):

```terminal
mkdir apps
mkdir apps/receitas
python manage.py startapp receitas ./apps/receitas
```

### 3.2 Registrando o app

Verificamos o nome do app no arquivo `apps/receitas/apps.py` e adicionamos na lista `INSTALLED_APPS` do arquivo `djangoreceitas/settings.py`. Se o app não estiver na raiz do projeto deve ser colocado o _dot path_ (_commit_ [3657009](https://github.com/brnocesar/alura/commit/36570099ac3a94c74e3e2ec56a92cf5801cad42a)).

### 3.3 Primeira rota

Devemos criar um arquivo de rotas para o app de receitas:

```terminal
touch apps/receitas/urls.py
```

Após isso podemos fazer os "importes" necessários e mapear a rota `/` desse grupo para o método `index()`, que será definido no arquivo `apps/receitas/views.py`, retornando uma resposta HTTP com um HTML.

E por último devemos registrar o arquivo de rotas do app receitas em `djangoreceitas/urls.py` (_commit_ [3d58da1](https://github.com/brnocesar/alura/commit/3d58da13210010a911102b90432c5f7d3eebff70)).

[↑ voltar ao topo](#django-receitas)

## 4 Arquivos estáticos

Podemos modificar o método `index()` no arquivo `apps/receitas/views.py` para ao invés de retornar uma resposta HTTP, retornar um arquivo HTML rendereizado. Então primeiro criamos o arquivo `apps/receitas/templates/index.html` que vai conter todo o HTML da página e modificamos o método `index()` (_commit_ [19845aa](https://github.com/brnocesar/alura/commit/19845aa1c577d5e82aab19fcc1f8f6a1c06e24fc)).

Agora podemos começar a adicionar o estilo das páginas HTML nos chamados **arquivos estáticos**. A primeira coisa a ser feita é especificar onde a apliacação deve procurar pelas páginas HTML. Como temos apenas um app, basta colocar o caminho da pasta `templates` desse app na lista mapeada para a chave `DIRS` do dicionário na lista `TEMPLATES` do arquivo de configurações do projeto (`djangoreceitas/settings.py`).

Ainda no arquivo de configurações, devemos especificar o local em que os arquivos estáticos vão ficar. No final do arquivo, perto de `STATIC_URL` adicionamos duas variáveis:

- `STATIC_ROOT`: local em que os arquivos estáticos vão ficar
- `STATICFILES_DIRS`: diretórios que contém os arquivos estáticos

não esqueça de adicionar o `import os.path` caso ele não esteja lá (_commit_ [e5ee498](https://github.com/brnocesar/alura/commit/e5ee498ac318286c6b7fd29072e0088a50e20d27)).

Após isso podemos de fato adicionar os arquivos estáticos em `djangoreceitas/static` (_commit_ [eca6e98](https://github.com/brnocesar/alura/commit/eca6e9812df32ca3008bdca7099ed57a6b872d1b)). E por último, "carregamos" os arquivos estáticos para a pasta `static` na raiz da aplicação. Nesse procedimento o Django faz uma cópia de todos arquivos estáticos da aplicação para essa pasta na raiz, para poder manipulá-los melhor (?):

```terminal
python manage.py collectstatic
```

É uma boa prática manter esses arquivos estáticos fora do repositório pois conforme nossa aplicação for crescendo, mais arquivos serão "copiados" para essa pasta. E também porque esse processo, em geral, é um dos passos realizados para o _deploy_ da aplicação (_commit_ [d856a11](https://github.com/brnocesar/alura/commit/d856a1118813dca2ba550276dfe3cc7f9bde8274)).

### 4.1 Definindo arquivos estáticos no HTML

Vamos adicionar arquivos HTML mais completos para o app de receitas, agora fazendo uso dos arquivos estáticos que foram adicionados (_commit_ [81492ec](https://github.com/brnocesar/alura/commit/81492ecb5d40350f0a0209713f00d9c1a276bca6)).

Para que o estilo seja aplicado nas páginas HTML é necessário informar ao Django que existem arquivos estáticos e isso é feito usando código Python (_commit_ [db95f53](https://github.com/brnocesar/alura/commit/db95f539eb4a65231fd335d21c578d236c698aa3)):

- na primeira linha do arquivo HTML adicionamos `{% load static %}`, que indica seram carregados arquivos estáticos
- em todas as referências de caminho devemos adicioná-las utilizando uma sintaxe específica para que o código Python possa ser interpretado: `{% static '<caminho relativo com extensão>' %}`
- também precisamos usar código Python para indicar os _links/URLs_: `{% url '<nome da rota>' %}`

[↑ voltar ao topo](#django-receitas)

### 4.2 Criando uma nova _view_

Vamos adicionar uma nova _view_ ao nosso _app_ e uma rota para acessá-la. No arquivo `apps/receitas/urls.py` adicionamos mais um `path()` na lista `urlpatterns`: definindo o _path_ da rota como `receita`, o método em `app/receitas/views.py` que vai retornar a página HTML renderizada e o nome da rota. Além disso temos que escrever o método `receita()` em `app/receitas/views.py`.

Para que seja possível acessar essa nova _view_ precisamos ainda "embedar" os _links_ em código Python (_commit_ [ab93b6e](https://github.com/brnocesar/alura/commit/ab93b6e4b30b141c5ba42070e813059833edc67f)).

### 4.3 Extendendo código HTML e _patials_

Pelos dois arquivos HTML que temos, podemos supor que a estrutura básica das páginas da nossa aplicação vai ser a igual para todas, compartilhando elementos como _header_ e _footer_. Então vamos separar todo esse código comum em arquivos próprios e fazer as _views_ "extenderem" esses arquivos.

Primeiro vamos criar nosso _layout_ base. No arquivo `apps/receitas/templates/base.html` copiamos todo conteúdo do arquivo `apps/receitas/templates/index.html` exceto o conteúdo dentro da _tag_ `<body>`, com exceção da declaração dos _scripts_ (deu pra entender...). Logo após a abertura da _tag_ `<body>` devemos indicar que ali vai "entrar" um bloco de código HTML, e fazemos isso através de código Python, `{% block content %} {% endblock %}`.

No arquivo `apps/receitas/templates/index.html` mantemos apenas as linhas que não foram copiadas para o _layout_ básico e indicamos que serão carregados arquivos estáticos (`{% load static %}`). Para tirar proveito do _layout_ base devemos extender este e "envelopar" seu conteúdo como um bloco (_commit_ [136f8d5](https://github.com/brnocesar/alura/commit/136f8d5249face18352eb5404dab55eb1b789783)). E podemos realizar o mesmo procedimento no arquivo `apps/receitas/templates/receita.html` (_commit_ [9a13d7a](https://github.com/brnocesar/alura/commit/9a13d7a1fd7a0358cd244a8dfa68ce43fe6a3890)).

Podemos "componentizar" ainda mais os elementos do nosso layout e das _views_ usando o resurso de _partials_. Eles são pequenos fragmentos de código HTML que podem ser compartilhados com várias _views_. Começamos criando a pasta `apps/receitas/templates/partials` e dentro dela arquivos para cada um dos _partials_ que vamos implementar, _header_ e _footer_. A partir disso basta copiar os respectivos códigos para cada arquivo, indicando que serão carregados arquivos estáticos. Para incluir os _partials_ usamos código Python `{% include 'partials/<nome do partial>.html' %}`. Note que o _partial_ do _footer_ foi adicionado apenas no _layout_ base, enquanto que o do _header_ precisou ser adicionado nas duas _views_ (_commit_ [193f407](https://github.com/brnocesar/alura/commit/193f40700c2fca38fe1ba14cc9f77e196df6a0b3)).

### 4.4 Apresentando informações de forma dinâmica

Agora vamos passar a enviar informações para a _view_, a partir do método que renderiza o HTML, e acessar essas informações. A primeira coisa a ser feita é modificar o método Python que renderiza a _view_, onde podemos passar uma coleção como terceiro parâmetro do método `render()`. E então na _view_ podemos usar código Python para iterar sobre essa coleção e acessar seus valores usando a notação `{{ variavel }}` (_commit_ [18fb6a5](https://github.com/brnocesar/alura/commit/18fb6a56e3a0db6cb6be93a63d41f9dd54c7feb1)).

[↑ voltar ao topo](#django-receitas)

## 5 Banco de Dados

Nesse ponto vamos configurar o Banco de dados da aplicação, que vai usar o PostgreSQL. Caso você não tenha familiaridade com esse SGDB ou com todos, após realizar o [download](https://www.postgresql.org/download/) e instalação, pode consultar este [apêndice](#criando-uma-base-de-dados-no-postgresql) para criar um usuário e a base de dados.

Para que a nossa aplicação consiga se conectar a um banco de dados PostgreSQL, devemos instalar um módulo Python que será responsável por intermediar essa conexão. Dentro do ambiente virtual rode o comando:

```terminal
pip install psycopg2-binary
```

E para finalizar a configuração do Banco de Dados, devemos colocar no arquivo `djangoreceitas/settings.py` as informações necessárias para que a aplicação saiba como se conectar ao Banco. Por padrão o SQLite já vem configurado, então basta trocar/adicionar as informações necessárias na váriavel `DATABASES` (_commit_ [b175afd](https://github.com/brnocesar/alura/commit/b175afdc8b2c84ee29011392fda9c3e0990c063a)).

[↑ voltar ao topo](#django-receitas)

## 6 _Models_ e _migrations_

Agora que já temos um banco de dados configurado, Vamos começar a utilizar o recurso das _models_, que é uma abstração para [modelgem](https://docs.djangoproject.com/en/3.1/topics/db/models/) e [consulta](https://docs.djangoproject.com/en/3.1/topics/db/queries/) dos dados em banco.

Um _model_ é uma classe Python que representa uma entidade do sistema, contendo seus atributos e comportamentos essenciais. Cada _model_ representa uma tabela no Banco de Dados, com seus atributos representando os campos da tabela e todas as _models_ no Django devem extender a classe `django.db.models.Model`.

Dentro do arquivo `apps/receitas/models.py` vamos definir a _model_ `Receita` e dentro dela definimos seus atributos. A partir da biblioteca `models` podemos definir o tipo de dados para cada campo e também as _constraints_ para esses campos, como o limite de caracteres, valor padrão ou se o campo aceita valor nulo (_commit_ [7fa5a09](https://github.com/brnocesar/alura/commit/7fa5a09286d9fef71764b1cf097926071b3bd6ab)).

Para mapear essa classe para uma tabela no banco de dados vamos usar o resurso de _migrations_. Com o comando abaixo criamos uma _migration_ a partir de alterações nas _models_ que ainda não estão mapeadas no Banco (_commit_ [99beaca](https://github.com/brnocesar/alura/commit/99beaca85df99f012ffa5a26fc9a92780b72f5e2)):

```terminal
python manage.py makemigrations
```

E para rodar as _migrations_ disponíveis:

```terminal
python manage.py migrate
```

[↑ voltar ao topo](#django-receitas)

## 7 Django Admin

O Django Admin é um dos recursos mais poderosos do _framework_ segundo a própia [documentação](https://docs.djangoproject.com/en/3.1/ref/contrib/admin/). É uma interface que permite a usuários com privilégios (_super users_) gerenciar os registros de entidades registradas para tal.

Em `djangoreceitas/urls.py` já existe uma rota configurada para o painel do **admin**, basta acessar `localhost:8000/admin`. Mas antes de logar é necessário criar um **_super user_**, para isso temos o comando:

```terminal
python manage.py createsuperuser
```

basta digitar as credências e dependendo da senha que você colocar o Django vai fornecer algumas orientações para criar uma senha mais segura.

Após logar no painel do **admin** percebemos que não há nada relacionado ao app `receitas`, para que seja disponibilizado o CRUD dessa entidade é necessário registrar o _model_ em `app/receitas/admin.py` (_commit_ [a372c7b](https://github.com/brnocesar/alura/commit/a372c7bb97854f502c05ec98b187ebf7aa8d5141)). Após isso, ao recarregar a página vemos que existe uma seção dedicada aos registros do app `receitas`.

[↑ voltar ao topo](#django-receitas)

## 8 Recuperando dados do Banco

### 8.1 Listando as receitas

Agora que temos dados de receitas armazenados no Banco de Dados podemos apresentá-los nas _views_. Para isso devemos alterar o dicionário passado por contexto para a _view_.  No método `index()` em `apps/receitas/views.py`, ao invés de passar um dicionário com valores no _hard coded_, vamos passar todos os objetos do tipo receita. Para isso vamos importar o _model_ `Receita` e usar o método `objects.all()` para recuperar todos os registros da tabela.

Devemos alterar a forma como é feito o acesso ao dicionário que a _view_ recebe, para que as receitas cadastradas através do Django Admin sejam apresentadas na _home_. Agora estamos enviando objetos, então podemos acessar seus atributos, e além disso, é uma boa prática verificar se a coleção de objetos não está vazia antes de iterar sobre ela (_commit_ [e444c74](https://github.com/brnocesar/alura/commit/e444c74ea7d48baeff4e18e0432870e15a3066ba)).

### 8.2 Detalhes de uma receita

Neste ponto, se clicamos em uma das receitas apresentadas na _home_ somos redirecionados para a _view_ "detalhes de uma receita", mas é a página genérica sem as informações da receita que queremos acessar.
Então precisamos de alguma forma indicar que queremos .

Para indicar que queremos acessar a página com as informações de uma receita específica devemos realizar algumas alterações:

- em `apps/receitas/templates/index.html` é necessário passar o identificador único da receita (atributo `id`) como parâmetro na URL: `<a href="{% url 'receita' valor_do_identificador %}">`
- na definição das rotas em `apps/receitas/urls.py`, devemos especificar que o recurso acessado será esse parâmetro que foi enviado pela URL: `'<int:receita_id>'`

Agora que temos acesso ao identificador único, que nesse caso é a chave primária da tabela de receitas, podemos receber esse parâmetro no método `receita()` em `apps/receitas/views.py`, recuperar o registro a partir da chave primária e passar o objeto para a _view_ (_commit_ [e21e83f](https://github.com/brnocesar/alura/commit/e21e83f82013506b68e4906db1c5b089186c8626)).

Por fim basta apresentar os atributos do objeto na _view_ receita (_commit_ [7fcb5d5](https://github.com/brnocesar/alura/commit/7fcb5d57f203dcf148ce49933caf62dc0300b9a3)).

[↑ voltar ao topo](#django-receitas)

## Apêndices

### Criando uma base de dados no PostgreSQL

Considerando que você já tem o PostgreSQL instalado em sua máquina, abaixo é apresentado um "passo a passo" para criar um usuário e uma base de dados para a aplicação. Os passos listados aqui foram executados na linha de comando e em ambiente Linux, então é possível que seja um pouco diferente para outras plataformas, mas a ideia geral permanece.

Primeiro vamos nos conectar ao servidor `postgres` com seu superusuário padrão, que é `postgres`:

```terminal
usuario@pc:~$ sudo -i -u postgres
postgres@pc:~$
```

Feito isso podemos nos conectar ao banco de dados:

```terminal
postgres@pc:~$ psql
psql (12.4 (Ubuntu 12.4-0ubuntu0.20.04.1))
Type "help" for help.

postgres=#
```

Agora vamos criar um usuário chamado `dev` com privilégios de _superuser_ e uma senha forte:

```terminal
postgres=# CREATE USER dev
postgres-# WITH SUPERUSER CREATEDB CREATEROLE
postgres-# PASSWORD '123456';
CREATE ROLE
postgres=#
```

Para se desconectar do _prompt_ do banco de dados digite `\q` e depois `exit` para retornar ao terminal do Linux:

```terminal
postgres=# \q
postgres@pc:~$ exit
sair
usuario@pc:~$
```

Agora que temos um usuário com privilégios para acessar a base de dados da nossa aplicação, vamos criá-la usando esse novo usuário. Começamos logando no servidor `postgres` no _localhost_ com o usuário chamado `dev` criado a pouco:

```terminal
usuario@pc:~$ psql -U dev -h 127.0.0.1 postgres
Password for user dev:
psql (12.4 (Ubuntu 12.4-0ubuntu0.20.04.1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.

postgres=#
```

Criamos uma base de dados chamada `django_receitas` definindo o usuário `dev` como _owner_:

```terminal
postgres=# CREATE DATABASE django_receitas WITH OWNER dev;
CREATE DATABASE
postgres=#
```

E para se conectar a essa base usamos o comando `\connect` passando seu nome:

```terminal
postgres=# \connect django_receitas;
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
You are now connected to database "django_receitas" as user "dev".
django_receitas=#
```

Para sair basta executar os mesmo comandos mostrados acima. [Voltar à configuração do banco.](#5-banco-de-dados).

[↑ voltar ao topo](#django-receitas)
