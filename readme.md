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
  4.3. Extendendo código HTML e _partials_  
  4.4. _Partials_  
  4.5. Apresentando informações de forma dinâmica  
5. [Banco de Dados](#5-banco-de-dados)  
6. [_Models_ e _migrations_](#6-_models_-e-_migrations_)  
  6.1 _Models_  
  6.2 _Migrations_  
7. [Django Admin](#7-django-admin)  
  7.1 Customizando apresentação de dados  
8. [Recuperando dados do Banco e apresentando nas _views_](#8-recuperando-dados-do-banco)  
  8.1 Listando as receitas  
  8.2 Detalhes de uma receita  
9. [Integrando apps](#9-integrando-apps)  
  9.1 Criando um novo app  
  9.2 Relacionamento _Many-to-one_  
10. [_Upload_ de arquivos](#10-_upload_-de-arquivos)  
  10.1 Imagens  
11. [Formulários](#11-Formulários)  
  11.1 App de usuários  
  11.2 Rotas de cadastro e _login_  
  11.3 Páginas de cadastro e _login_  
  11.4 Requisições de formulários  
  11.4.1 Enviando o formulário  
  11.4.2 Acessando os campos de um formulário  
  11.5 Cadastrando novo usuário  
  11.6 Realizando _login_  
  11.7 Formulário para receitas  
12. [Mensagens de _feedback_](#11-Mensagens-de-_feedback_)  

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

- Lista de comandos disponíveis na _cli_ do Django:

```terminal
django-admin help
```

- Criando o projeto da aplicação (_commit_ [938745e](https://github.com/brnocesar/django-receitas/commit/938745e0a1f78395e8be1b5e88af6b2fcd47de6a)):

```terminal
django-admin startproject djangoreicetas .
```

- Subindo o servidor:

```terminal
python manage.py runserver
```

[↑ voltar ao topo](#django-receitas)

## 3 Apps

Os Apps do Django podem ser entendidos como "sub-aplicações" com a finalidade de representar domínios da aplicação. No sistema desenvolvido aqui, por exemplo, vamos ter um app resposável por todo o gerenciamento das receitas.

Um projeto é uma coleção de configurações e apps que formam um _site_; e um app é uma "sub-aplicação" com uma finalidade/responsabilidade bem definida, podendo fazer parte de vários projetos.

### 3.1 Criando um app

Criando um app na raiz da aplicação:

```terminal
python manage.py startapp receitas
```

Para criar o app dentro de uma pasta dedicada, primeiro devemos criar essa pasta e então podemos passar como segundo parâmetro o caminho onde o app deverá ser criado (_commit_ [60f0ad1](https://github.com/brnocesar/django-receitas/commit/60f0ad14ef51e6229afb3b0ad0738d0db721cf64)):

```terminal
mkdir apps
mkdir apps/receitas
python manage.py startapp receitas ./apps/receitas
```

### 3.2 Registrando o app

Verificamos o nome do app no arquivo `apps/receitas/apps.py` e adicionamos na lista `INSTALLED_APPS` do arquivo `djangoreceitas/settings.py`. Se o app não estiver na raiz do projeto deve ser colocado o _dot path_ (_commit_ [3657009](https://github.com/brnocesar/django-receitas/commit/36570099ac3a94c74e3e2ec56a92cf5801cad42a)).

### 3.3 Primeira rota

Devemos criar um arquivo de rotas para o app de receitas:

```terminal
touch apps/receitas/urls.py
```

Após isso podemos fazer os "importes" necessários e mapear a rota `/` desse grupo para o método `index()`, que será definido no arquivo `apps/receitas/views.py`, retornando uma resposta HTTP com um HTML.

E por último devemos registrar o arquivo de rotas do app receitas em `djangoreceitas/urls.py` (_commit_ [3d58da1](https://github.com/brnocesar/django-receitas/commit/3d58da13210010a911102b90432c5f7d3eebff70)).

[↑ voltar ao topo](#django-receitas)

## 4 Arquivos estáticos

Podemos modificar o método `index()` no arquivo `apps/receitas/views.py` para ao invés de retornar uma resposta HTTP, retornar um arquivo HTML rendereizado. Então primeiro criamos o arquivo `apps/receitas/templates/index.html` que vai conter todo o HTML da página e modificamos o método `index()` (_commit_ [19845aa](https://github.com/brnocesar/django-receitas/commit/19845aa1c577d5e82aab19fcc1f8f6a1c06e24fc)).

Agora podemos começar a adicionar o estilo das páginas HTML nos chamados **arquivos estáticos**. A primeira coisa a ser feita é especificar onde a apliacação deve procurar pelas páginas HTML. Como temos apenas um app, basta colocar o caminho da pasta `templates` desse app na lista mapeada para a chave `DIRS` do dicionário na lista `TEMPLATES` do arquivo de configurações do projeto (`djangoreceitas/settings.py`).

Ainda no arquivo de configurações, devemos especificar o local em que os arquivos estáticos vão ficar. No final do arquivo, perto de `STATIC_URL` adicionamos duas variáveis:

- `STATIC_ROOT`: local em que os arquivos estáticos vão ficar
- `STATICFILES_DIRS`: diretórios que contém os arquivos estáticos

não esqueça de adicionar o `import os.path` caso ele não esteja lá (_commit_ [e5ee498](https://github.com/brnocesar/django-receitas/commit/e5ee498ac318286c6b7fd29072e0088a50e20d27)).

Após isso podemos de fato adicionar os arquivos estáticos em `djangoreceitas/static` (_commit_ [eca6e98](https://github.com/brnocesar/django-receitas/commit/eca6e9812df32ca3008bdca7099ed57a6b872d1b)). E por último, "carregamos" os arquivos estáticos para a pasta `static` na raiz da aplicação. Nesse procedimento o Django faz uma cópia de todos arquivos estáticos da aplicação para essa pasta na raiz, para poder manipulá-los melhor:

```terminal
python manage.py collectstatic
```

É uma boa prática manter esses arquivos estáticos fora do repositório pois conforme nossa aplicação for crescendo, mais arquivos serão "copiados" para essa pasta. E também porque esse processo, em geral, é um dos passos realizados para o _deploy_ da aplicação (_commit_ [d856a11](https://github.com/brnocesar/django-receitas/commit/d856a1118813dca2ba550276dfe3cc7f9bde8274)).

### 4.1 Definindo arquivos estáticos no HTML

Vamos adicionar arquivos HTML mais completos para o app de receitas, agora fazendo uso dos arquivos estáticos que foram adicionados (_commit_ [81492ec](https://github.com/brnocesar/django-receitas/commit/81492ecb5d40350f0a0209713f00d9c1a276bca6)).

Para que o estilo seja aplicado nas páginas HTML é necessário informar ao Django que existem arquivos estáticos e isso é feito usando código Python (_commit_ [db95f53](https://github.com/brnocesar/django-receitas/commit/db95f539eb4a65231fd335d21c578d236c698aa3)):

- na primeira linha do arquivo HTML adicionamos `{% load static %}`, indicando que seram carregados arquivos estáticos
- em todas as referências de caminho devemos adicioná-las utilizando uma sintaxe específica para que o código Python possa ser interpretado: `{% static '<caminho relativo com extensão>' %}`
- também precisamos usar código Python para indicar os _links/URLs_: `{% url '<nome da rota>' %}`

[↑ voltar ao topo](#django-receitas)

### 4.2 Criando uma nova _view_

Vamos adicionar uma nova _view_ ao nosso _app_ e uma rota para acessá-la. No arquivo `apps/receitas/urls.py` adicionamos mais um `path()` na lista `urlpatterns` definindo na ordem: o recurso da rota como `receita`, o método em `app/receitas/views.py` que vai retornar a página HTML renderizada e o nome da rota. Além disso, obviamente temos que escrever o método `receita()` em `app/receitas/views.py` retornando essa _view_.

Para que seja possível acessar essa nova _view_ precisamos ainda "embedar" os _links_ em código Python (_commit_ [ab93b6e](https://github.com/brnocesar/django-receitas/commit/ab93b6e4b30b141c5ba42070e813059833edc67f)).

### 4.3 Extendendo código HTML

Pelos dois arquivos HTML que temos, podemos supor que a estrutura básica das páginas da nossa aplicação vai ser a igual para todas, compartilhando elementos como _header_ e _footer_. Então vamos separar todo esse código comum em arquivos próprios e fazer as _views_ "extenderem" esses arquivos.

Primeiro vamos criar nosso _layout_ base. No arquivo `apps/receitas/templates/base.html` copiamos todo conteúdo do arquivo `apps/receitas/templates/index.html` exceto o conteúdo dentro da _tag_ `<body>`, com exceção da declaração dos _scripts_ (deu pra entender...). Logo após a abertura da _tag_ `<body>` devemos indicar que ali vai "entrar" um bloco de código HTML, e os delimitadores desse bloco são escritos em código Python: `{% block content %} {% endblock %}`.

No arquivo `apps/receitas/templates/index.html` mantemos apenas as linhas que não foram copiadas para o _layout_ básico e a indicação que serão carregados arquivos estáticos (`{% load static %}`). Para tirar proveito do _layout_ base devemos extender este (`{% extends 'base.html' %}`) e "envelopar" seu conteúdo como um bloco usando os delimitadores mencionados no parágrafo anterior (_commit_ [136f8d5](https://github.com/brnocesar/django-receitas/commit/136f8d5249face18352eb5404dab55eb1b789783)). E podemos realizar o mesmo procedimento para a _view_ de receitas (_commit_ [9a13d7a](https://github.com/brnocesar/django-receitas/commit/9a13d7a1fd7a0358cd244a8dfa68ce43fe6a3890)).

### 4.4 _Partials_

Podemos "componentizar" ainda mais os elementos do nosso layout usando o resurso de _partials_, pequenos fragmentos de código HTML que podem ser compartilhados com várias _views_.

Começamos criando a pasta `apps/receitas/templates/partials` e dentro dela teremos arquivos para cada um dos _partials_ que vamos implementar, _header_ e _footer_. A partir disso basta copiar os respectivos códigos para cada arquivo, indicando que serão carregados arquivos estáticos. Para incluir os _partials_ usamos código Python `{% include 'partials/<nome do partial>.html' %}`. Note que o _partial_ do _footer_ foi adicionado apenas no _layout_ base, enquanto que o do _header_ precisou ser adicionado nas duas _views_ (_commit_ [193f407](https://github.com/brnocesar/django-receitas/commit/193f40700c2fca38fe1ba14cc9f77e196df6a0b3)).

Uma conveção bastante adotada é nomear as _partials_ começando com um _underline_, tornando claro do que se trata o arquivo. Neste projeto o "_layout_ base" também foi nomeado seguindo dessa forma (_commit_ [7faee76](https://github.com/brnocesar/django-receitas/commit/7faee768ca20b8c6bf20ddc40a18e3de26fadbfa)).

### 4.5 Apresentando informações de forma dinâmica

Agora vamos passar a enviar informações para a _view_ a partir do método que renderiza o HTML e acessa-lás. A primeira coisa a ser feita é modificar o método Python que renderiza a _view_, onde podemos passar uma coleção como terceiro parâmetro do método `render()`. E então na _view_ podemos usar código Python para iterar sobre essa coleção e acessar seus valores usando a notação `{{ variavel }}` (_commit_ [18fb6a5](https://github.com/brnocesar/django-receitas/commit/18fb6a56e3a0db6cb6be93a63d41f9dd54c7feb1)).

[↑ voltar ao topo](#django-receitas)

## 5 Banco de Dados

Nesse ponto vamos configurar o Banco de dados da aplicação, que vai usar o PostgreSQL. Caso você não tenha familiaridade com esse SGDB ou com todos, após realizar o [download](https://www.postgresql.org/download/) e instalação, pode consultar este [apêndice](#criando-uma-base-de-dados-no-postgresql) para criar um usuário e a base de dados.

Para que a nossa aplicação consiga se conectar a um banco de dados PostgreSQL, devemos instalar um módulo Python que será responsável por intermediar essa conexão. Dentro do ambiente virtual rode o comando:

```terminal
pip install psycopg2-binary
```

E para finalizar a configuração do Banco de Dados, devemos colocar no arquivo `djangoreceitas/settings.py` as informações necessárias para que a aplicação saiba como se conectar ao Banco. Por padrão o SQLite já vem configurado, então basta trocar/adicionar as informações necessárias na váriavel `DATABASES` (_commit_ [b175afd](https://github.com/brnocesar/django-receitas/commit/b175afdc8b2c84ee29011392fda9c3e0990c063a)).

[↑ voltar ao topo](#django-receitas)

## 6 _Models_ e _migrations_

### 6.1 _Models_

Agora que já temos um banco de dados configurado, Vamos começar a utilizar o recurso das _models_, que é uma abstração para [modelgem](https://docs.djangoproject.com/en/3.1/topics/db/models/) e [consulta](https://docs.djangoproject.com/en/3.1/topics/db/queries/) dos dados em banco.

Um _model_ é uma classe Python que representa uma entidade do sistema, contendo seus atributos e comportamentos essenciais. Cada _model_ representa uma tabela no Banco de Dados, com seus atributos representando os campos da tabela e todas as _models_ no Django devem extender a classe `django.db.models.Model`.

Dentro do arquivo `apps/receitas/models.py` vamos definir a _model_ `Receita` e dentro dela definimos seus atributos. A partir da biblioteca `models` podemos definir o tipo de dados para cada campo e também as _constraints_ para esses campos, como o limite de caracteres, valor padrão ou se o campo aceita valor nulo (_commit_ [7fa5a09](https://github.com/brnocesar/django-receitas/commit/7fa5a09286d9fef71764b1cf097926071b3bd6ab)).

Podemos definir a representação textual de um objeto utilizando o método especial `__str__` (_dunder methods_) e alterar a forma como são acessados nas _views_ (_commit_ [79a272e](https://github.com/brnocesar/django-receitas/commit/79a272e606c33bd374223185089a1cf2f0fd3ccc)).

### 6.2 _Migrations_

Para fazer o mapeamento des classes do tipo _model_ para tabelas no banco de dados usamos o recurso de _migrations_. Com o comando abaixo criamos uma _migration_ a partir de alterações nas _models_ que ainda não estão mapeadas no Banco (_commit_ [99beaca](https://github.com/brnocesar/django-receitas/commit/99beaca85df99f012ffa5a26fc9a92780b72f5e2)):

```terminal
python manage.py makemigrations
```

Após rodar esse comando, por exemplo, a _migration criada agora será responsável apenas por criar a tabela de nome `receitas_receita` (_model_ receita no app receitas) com os campos correspondentes aos atributos que a model possui nesse momento.

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

Após logar no painel do **admin** percebemos que não há nada relacionado ao app `receitas`, para que seja disponibilizado o CRUD dessa entidade é necessário registrar o _model_ em `app/receitas/admin.py` (_commit_ [a372c7b](https://github.com/brnocesar/django-receitas/commit/a372c7bb97854f502c05ec98b187ebf7aa8d5141)). Ao recarregar a página vemos que existe uma seção dedicada aos registros do app `receitas`.

### 7.1 Customizando apresentação de dados

Podemos customizar a forma como as receitas são apresentadas no Django Admin. Por exemplo, apresentando mais atributos e tornando alguns links para suas receitas. Também é podemos habilitar algumas funcionalidades como filtros, buscas e paginação. Para isso criamos uma classe em `apps/receitas/admin.py` extendendo `admin.ModelAdmin` e definimos as alterações que quisermos (_commit_ [cb855da](https://github.com/brnocesar/django-receitas/commit/cb855daac4f4385ffb7567ad9c18889cc4588720)), não esquecendo de também registrar essa classe.

É possível ainda editar alguns campos dos registros diretamente na página de listagem, para isso definimos a variável `list_editable` em `apps/nome_do_app/admin.py` atribuindo uma tupla ou lista com os campos que queremos permitir a edição (_commit_ [c1eddb8](https://github.com/brnocesar/django-receitas/commit/c1eddb83f202b158a1ec92c45a4e4e86f8090348)).

[↑ voltar ao topo](#django-receitas)

## 8 Recuperando dados do Banco

### 8.1 Listando as receitas

Agora que temos dados de receitas armazenados no Banco de Dados podemos apresentá-los nas _views_. Para isso devemos alterar o dicionário passado por contexto para a _view_.  No método `index()` em `apps/receitas/views.py`, ao invés de passar um dicionário com valores _hard coded_, vamos passar todos os objetos do tipo receita que foram cadastrados. Para isso vamos importar o _model_ `Receita` e usar o método `objects.all()` para recuperar todos os registros da tabela.

Devemos alterar a forma como é feito o acesso ao dicionário que a _view_ recebe, para que as receitas cadastradas através do Django Admin sejam apresentadas na _home_. Agora estamos enviando objetos, então podemos acessar seus atributos, e além disso, é uma boa prática verificar se a coleção de objetos não está vazia antes de iterar sobre ela (_commit_ [e444c74](https://github.com/brnocesar/django-receitas/commit/e444c74ea7d48baeff4e18e0432870e15a3066ba)).

Podemos utilizar filtros para selecionar os registros que serão recuperados do banco e enviados para a _view_, assim como podemos ordenar os registros recuperados em função de um campo de forma ascendente ou descendente (_commits_ [ad40637](https://github.com/brnocesar/django-receitas/commit/ad40637edce8d62934a742c9ae7283c2fcdc223f) e [e94e15c](https://github.com/brnocesar/django-receitas/commit/e94e15cfcb46b1607fc639eba90f16315dfa0b90)).

### 8.2 Detalhes de uma receita

Neste ponto, se clicamos em uma das receitas apresentadas na _home_ somos redirecionados para a _view_ "detalhes de uma receita", mas é a página genérica sem as informações da receita que queremos acessar. Então precisamos indicar qual é a receita correta.

Para indicar que queremos acessar a página com as informações de uma receita específica devemos realizar algumas alterações:

- em `apps/receitas/templates/index.html` é necessário passar o identificador único da receita (atributo `id`) como parâmetro na URL: `<a href="{% url 'receita' valor_do_identificador %}">`
- na definição das rotas em `apps/receitas/urls.py`, devemos especificar que o recurso acessado será esse parâmetro que foi enviado pela URL: `'<int:receita_id>'`

Agora que temos acesso ao identificador único, que nesse caso é a chave primária da tabela de receitas, podemos receber esse parâmetro no método `receita()` em `apps/receitas/views.py`, recuperar o registro a partir da chave primária e passar o objeto para a _view_ (_commit_ [e21e83f](https://github.com/brnocesar/django-receitas/commit/e21e83f82013506b68e4906db1c5b089186c8626)).

Por fim basta apresentar os atributos do objeto na _view_ receita (_commit_ [7fcb5d5](https://github.com/brnocesar/django-receitas/commit/7fcb5d57f203dcf148ce49933caf62dc0300b9a3)).

[↑ voltar ao topo](#django-receitas)

## 9 Integrando apps

As receitas são cadastradas por pessoas, então vamos criar um novo app para gerenciar as **pessoas** da aplicação e depois integrá-lo com o app de receitas.

### 9.1 Criando um novo app

Todo o procedimento é o mesmo que foi feito para o app de receitas e a entidade Receita. Primeiro criamos o novo app e o registramos na aplicação adicionando-o na váriavel `INSTALLED_APPS` de `djangoreceitas/settings.py`.

Criamos a classe para representar a entidade Pessoa em `apps/pessoas/models.py` e a registramos para ser gerenciada pelo Admin em `apps/pessoas/admin.py`, aproveitando para customizar a página de listagem.

E por fim, geramos as _migrations_ e a executamos (_commit_ [d502182](https://github.com/brnocesar/django-receitas/commit/d502182088b58dbd1d348e1415b0497c51cfce17)).

### 9.2 Relacionamento _Many-to-one_

Vamos definir o relacionamento entre receitas e pessoas, no caso cada pessoa pode cadastrar várias receitas e cada receita pertence a uma única pessoa. Esse tipo de relacionamento é chamado de "um para muitos" e é definido através de uma chave estrangeira, nesse caso será uma chave estrangeira na tabela de receitas apontando para a tabela de pessoas.

Adicionamos um novo campo na _model_ Receita, do tipo _ForeigKey_ e nomeando-o de acordo com a convenção sugerida na [documentação](https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-one-relationships). Geramos a _migration_ para essa alteração e a executamos (_commit_ [e157988](https://github.com/brnocesar/django-receitas/commit/e157988bce56bb393326b9ee11a88dec2bb4f207)).

[↑ voltar ao topo](#django-receitas)

## 10 _Upload_ de arquivos

### 10.1 Imagens

Vamos começar a implementar a funcionalidade de _upload_ de arquivos definindo as configurações necessárias para a aplicação. Em `djangoreceitas/settings.py` vamos criar duas variáveis: `MEDIA_ROOT` vai armazenar o local/diretório onde os arquivos serão armazenados e `MEDIA_URL` é o recurso a partir do qual será possível acessar as imagens pela URL.

Ao criar o novo campo na _model_ Receita definimos o tipo do campo como `ImageField` e passamos o local relativo a `MEDIA_ROOT` em que as imagens devem ser armazenadas.

Antes de gerar e rodar a _migration_ precisamos instalar um pacote necessário para trabalhar com os arquivos de imagens:

```terminal
pip install pillow
```

então podemos atualizar o banco (_commit_ [74caf89](https://github.com/brnocesar/django-receitas/commit/74caf893e543512c25603e82be1baf4ccad1a211)).

Para que seja possível apresentar essas imagens nas _views_, devemos permitir que suas URLs sejam utilizadas pela aplicação e isso é feito indicando o uso das configurações de mídia no arquivo de rotas da aplicação em `djangoreceitas/urls.py`. Após isso podemos modificar as _views_ para apresentar as imagens de cada receita (_commit_ [348567b](https://github.com/brnocesar/django-receitas/commit/348567b18a4e1370b6581b7423416fb9b557b07e)).

[↑ voltar ao topo](#django-receitas)

## 11 Formulários

Se verificarmos o banco de dados da aplicação vamos encontrar uma tabela chamada `auth_user`. Nessa tabela são armazenados todos os usuários do sistema, desde os comuns até os _superusers_, com acesso ao Django Admin. Os super-usuários já podem ser criados através da linha de comando, então vamos criar um app de usuários para permitir que novos usuários se cadastrem no sistema sem precisar do privélio de ser um super-usuário. E para isso vamos precisar de páginas com formulários específicos para essas ações

### 11.1 App de usuários

O procedimento para criar um novo app dentro da pasta `apps` é: primeiro criar a pasta do novo app e então rodar o comando com passando este _path_:

```terminal
mkdir apps/usuarios
python manage.py startapp usuarios ./apps/usuarios
```

após isso ainda é necessário registrar o app nas configurações da aplicação adicionando-o na lista `INSTALLED_APPS` (_commit_ [850190d](https://github.com/brnocesar/django-receitas/commit/850190db6f5b40d6087e126cb9fea6e85826a323)).

### 11.2 Rotas de cadastro e _login_

Vamos começar essa parte tratando das rotas. Criamos o arquivo de rotas (`apps/usuarios/urls.py`) para o app, definimos os recursos acessados para as páginas e registramos essas rotas nas urls da aplicação (`djangoreceitas/urls.py`). Note que podemos definir um prefixo para as rotas do app (_commit_ [ccce69a](https://github.com/brnocesar/django-receitas/commit/ccce69a590e9697fc877e2382e3e914cb2cab3e4)).

### 11.3 Páginas de cadastro e _login_

Antes de iniciar a implementação da primeira página que é a de cadastro, precisamos lidar com os templates base. O template básico e os _partials_ foram definidos dentro do app de receitas, mas agora que a aplicação está crescendo e temos mais apps que faram uso desses recursos devemos mover essa pasta. O ideal é que os templates fiquem no mesmo nível dos apps e não dentro de um deles, então movemos a pasta `templates` de `apps/receitas` para `apps`. Além disso devemos alterar o local da pasta `templates` nas configurações da aplicação (_commit_ [c7bbedf](https://github.com/brnocesar/django-receitas/commit/c7bbedfa2786c704a139405e64ee921fa8e19382)).

Para organizar melhor as _views_ podemos criar pastas para cada um dos apps dentro de `templates`, lembrando de indicar a pasta ao retornar a _view_, começando com as páginas do app de receitas (_commit_ [f0d35cc](https://github.com/brnocesar/django-receitas/commit/f0d35ccaaf230e2bfafb4b384b5a1837f909c297)) e depois com as paǵinas de usuários (_commit_ [13d0c6a](https://github.com/brnocesar/django-receitas/commit/13d0c6a9918286cb2d72a02c6d750b5c2039e01f)).

### 11.4 Requisições de formulários

#### 11.4.1 Enviando o formulário

Agora que já temos uma página para os formulários podemos começar a pensar em como enviar as informações nele preenchidas e como acessá-las na nossa aplicação.

A primeira coisa que faremos é especificar o tipo de requisição em que o formulário será submetido, como se tratam de informações sensíveis (senha) precisamos utilizar o método `POST` para a requisição, definindo isso no atributo `method` da _tag_ `<form>`. Após isso definimos para onde a requisição do formulário será enviada, passando o nome da rota através de código Python. Além disso devemos incluir o _token_ CSRF dentro do formulário para garantir que a requisição está sendo enviada pela nossa aplicação.

```python
<form action="{% url 'nome_da_rota' %}" method="POST">
    {% csrf_token %}
    ...
</form>
```

Ao contrário de outros _frameworks_ em que você define o método de acesso da requisição para cada rota, no Django mapeamos apenas a rota para um método (código que será  executado) e dentro do código devemos verificar o tipo de método (requisição) para decidir o que fazer.

#### 11.4.2 Acessando os campos de um formulário

Agora que estamos conseguindo enviar o formulário com os campos preenchidos, podemos acessar esses campos no método (código) mapeado para a rota definida como `action` do formulário. Dentro desse método temos acesso à requisição através do objeto `request` obtido por injeção de dependência. Como a requisição foi feita usando o método `POST`, dentro do atributo de mesmo nome vamos acessar um dicionário com todos os campos enviados (_commit_ [c5b1601](https://github.com/brnocesar/django-receitas/commit/c5b160139502536430e2760b569ac7d8f5a4b990)):

```python
request.POST
```

### 11.5 Cadastrando novo usuário

Como estamos usando uma tabela criada pelo Django, podemos importar o model que modela a tabela de usuários e utilizar _built in functions_ para adicionar um novo usuário no sistema (não precisamos nem "encriptar" a senha). Antes disso podemos fazer validações básicas sobre os dados que estamso recebendo do formulário (_commit_ [a663965](https://github.com/brnocesar/django-receitas/commit/a6639650d9401785d39275c8e685a8a79c5bf88a)).

### 11.6 Realizando _login_

O processo de autenticação de um usuário começa com o formulário de _login_ e devemos enviar seus campos para o código que irá processar essa ação, esse processo é muito similar ao cadastro de novos usuários. Como a forma padrão de autenticação do Django é feita em função dos valores de `username` e senha, após nos certificarmos que os valores obtidos do formulário são válidos, precisamos obter o `username` do usuário. Então podemos realizar o _login_ caso o usuário exista e redirecioná-lo para sua _dashboard_ (_commit_ [4f42d15](https://github.com/brnocesar/django-receitas/commit/4f42d15eaf95a11042c08495a2166f09055ecd9b)).

Agora podemos fazer alguns ajustes no _layout_ de modo que os botões do _header_ façam mais sentido para usuários logados, implementar a funcionalidade de _logout_ e impedir que usuários não autenticados não acessem algumas páginas (_commit_ [9c3a304](https://github.com/brnocesar/django-receitas/commit/9c3a3044a79c310f38ea995e3e7edba5a38b1555)).

### 11.7 Formulário para receitas

Vamos montar um formulário para os usuários autenticados sejam capazes de cadastrar suas receitas, então precisamos criar a rota e a _view_ com o formulário (_commit_ [21c69f3](https://github.com/brnocesar/django-receitas/commit/21c69f3e68f6891d6abd82e0c1bbab89d7ef9155)).

Anteriormente quando a única forma de cadastro de receitas era através do Django Admin, relacionamos as receitas com a classe `Pessoa`. Agora que usuários autenticados podem cadastrar receitas na aplicação, vamos relacionar as receitas com a classe `User`. Para isso basta importar a _model_ de usuário e substituir na declaração do atributo `pessoa`. Para que essa alteração tenha efeito no Banco precisamos gerar uma _migration_ com as alterações e executá-la (_commit_ [3eee356](https://github.com/brnocesar/django-receitas/commit/3eee356baa4a1b1de761df287fdafae277536e5c)). Os comandos necessários são:

```terminal
python manage.py makemigrations
python manage.py migrate
```

Agora podemos receber os campos do formulário e criar um novo registro do tipo `Receita`. Com exceção do campo `foto`, todos os campos ficam disponíveis no dicionário do atributo `POST` do objeto `request`. A foto foi enviada através de um _input_ do tipo arquivo, então a acessamos no atributo `FILES`. Para criar um registro do tipo Receita usamos o método `create` passando cada um dos campos recebidos na requisição e então salvamos o objeto criado (_commit_ [1b4275f](https://github.com/brnocesar/django-receitas/commit/1b4275f5ed72759ab2aec884c70e2dc04c535fbb)).

Após realizar o cadastro da nova receita, redirecionamos o usuário para sua _dashboard_ onde serão apresentadas apenas as suas receitas (_commit_ [13d19cc](https://github.com/brnocesar/django-receitas/commit/13d19cc3d04730188a371a81cb07d16b538faa23)).

## 12 Mensagens de alerta

O Django já nos fornece um sistema de [mensagens](https://docs.djangoproject.com/en/3.1/ref/contrib/messages/) de alerta (_feedback messages_) com vários níveis/tipos que podems ser definidos através da variável `MESSAGE_TAGS` em `djangoreceitas/settings.py`. Podemos aproveitar o estilo das caixas de alertas do [Bootstrap](https://getbootstrap.com/docs/4.0/components/alerts/) e definir as _tags_ de mensagens em função dessas classes.

Também precisamos criar um componente (_partial_) que irá conter o HTML da mensagem de alerta e podemos adicioná-lo no _layout_ base (_commit_ [b50c0a9](https://github.com/brnocesar/django-receitas/commit/b50c0a97261990faaafcf79cbe6678364cf75177)). Após isso podemos definir as mensagens com o devido tipo e conteúdo de acordo com a situação (_commit_ [3e2e7fe](https://github.com/brnocesar/django-receitas/commit/3e2e7fe826a4751962bcb9e4eacb26087b52a6b5)).

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
