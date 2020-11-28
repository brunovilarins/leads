# Leads

Projeto para captação de leads e seleção de agentes.

# Requisitos

  - [Docker](https://docs.docker.com/engine/install/) - Manual de instalação
  - [Docker Compose](https://docs.docker.com/compose/install/) - Manual de instalação
  - Git

# Instalação


### Executando o projeto

```sh
# Clonar o projeto do github
$ git clone https://github.com.br/brunovilarins/leads

# Entrar na pasta do projeto
$ cd leads

# Executar a criação dos containers e start do projeto
$ docker-compose up -d --build

# Verificar se os serviços estão executando
$ docker-compose ps
#lead-api      ...   Up      0.0.0.0:8000->8000/tcp
#lead-database ...   Up      0.0.0.0:5432->5432/tcp
```
> Com os serviços ativos, abra o navegador e acesse o endereço http://localhost:8000 para acessar a documentação da API.

> Caso os comandos do **docker-compose** não tenha permissão, adicionar **sudo** no início do comando.


### Executando testes automatizados
```sh
# Executar os testes automatizados
$ docker-compose exec lead-api pytest
......
```

### Destruindo os containers
```sh
# Remover os containers e apagar os volumes criados
$ docker-compose down -v
```

