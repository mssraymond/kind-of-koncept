FROM confluentinc/cp-kafka-connect:7.5.2

USER root

RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:2.2.1

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.8.0

RUN curl -L -o /usr/share/java/kafka/postgresql.jar \
  https://jdbc.postgresql.org/download/postgresql-42.6.1.jar