FROM confluentinc/cp-kafka-connect:latest

USER root

RUN curl -L -o /usr/share/java/kafka/postgresql.jar \
  https://jdbc.postgresql.org/download/postgresql-42.7.3.jar

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:latest

RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:latest