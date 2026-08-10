# Monitoramento de Redde

Esse projeto tem como objetivo monitorar alguns parâmetros de rede e verificar a qualidade de internet.

**Parâmetros Utilizados**

- Conexão com a provedora de internet
- Velocidade de Downloads e Upload pela provedora
- Conexão com servidores de DNS
- Instabilidade com os servidores de DNS
- Velocidade de Donwload de serviços em nuvem
- Perda de pacotes da conexão de internet
- Monitoramento de aplicações Web

Esse projeto possui várias aplicações para analisar, armazenar e visualizar os parâmetros estudados. Por questão de praticidade foi adotado o Docker compose que utiliza vários containers e possibilita a pre-configurações dos mesmos, trazendo também a portabilidade tanto para arquiteturas ARM quanto para AMD(x86). Para usar o projeto instale o **DOCKER COMPOSE** no seu sistema operacional. Baixe o repositório e em seguida suba os containers. 

```bash
docker compose up -d





