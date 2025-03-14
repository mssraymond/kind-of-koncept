# Kind of Koncept (aka. POC w/ kind) 😜

## Architecture

[--- Python ---] --> [--- Kafka ---] --> [--- JDBC Sink Connector] --> [--- PostgreSQL ---] --> [--- Debezium Source Connector ---] --> [--- Kafka ---] [--- Spark ---]

[------------------------------------------------------------------------------ Kubernetes ---------------------------------------------------------------------------]

## Prerequisites

- [Docker](https://docs.docker.com/engine/install/)
- [Kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)

## Walkthrough

1. Start up: `./scripts/start`
2. Check status: `./scripts/status`
3. View pgAdmin at `localhost:5050`
    - *LOGIN (password "postgres")* ![login](imgs/img_1.png)
    - *CONNECT* ![connect](imgs/img_2.png)
    - *UPLOAD* ![upload_1](imgs/img_3.png) ![upload_2](imgs/img_4.png) ![upload_3](imgs/img_5.png)
    - *QUERY* ![query](imgs/img_6.png)
4. View Kafka UI at `localhost:5051`
    - *TOPIC (JDBC Sink Connector)* ![topic](imgs/img_7.png)
    - *TOPIC (Debezium Source Connector)* ![topic](imgs/img_8.png)
    ***If `debezium.public.loggings` topic doens't show up or isn't ingesting more messages, run `./script/dbzm` to reboot the connector.**
5. Shut down: `./scripts/stop`
