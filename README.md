
# Ps impar

API desenvolvida para o processo seletivo da empresa ímpar:

## Get Started

Essa api foi construido com para o cadastro de carros em um DB postgres.
Foram criados 4 endpoints com o objetivo de manipular esses dados. 


## A estrutura
```
|- api/  
|   |- database/
|   |- models/
|   |- routes/
|   |- schemas/
|   |- config.py
|   |- main.py
|- docker-compose.yml 
|- Dockerfile  
|- README.md  
|- requeriments.txt
|- .env.exemple
```
### Database 
Contém 2 arquivos:

connection_database.py: responsavel por criar a conexão com a base de dados;
crud: responsavel pela operações na base de dados; 

### models
Contém os modelos da base de dados;

### routes
Responsavel por gerir as rotas da api, contém 2 arquivos. 1 para os endpoints de carros e um para o endpoint de photos.

### schema 
Contém os esquemas utilizados pela nossa api. 

### config.py 
Responsavel peela leitura de qualquer variável que a API possa precisar ou qualquer outra operação extra.

### main.py 
função principal da api, que conecta todos os pontos para que ela possa funcionar.

### Dockerfile
Configura um container para que nossa api rode como um microsserviço.

### docker-compose.yml
Inicia nossos serviços, nele subi um banco de testes que acabei usando durante todo o processo, pois tive algumas dificuldades em conectar ao db fornecido.

### requeriments.txt 
Todas as bibliotecas que nossa api precisa para rodar.

### .env.exemple
Exemplo de configuração do .env da aplicação
