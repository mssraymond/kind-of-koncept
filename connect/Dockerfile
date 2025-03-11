FROM confluentinc/cp-kafka-connect:7.6.0

USER root

RUN curl -L -o /usr/share/java/kafka/postgresql.jar \
  https://jdbc.postgresql.org/download/postgresql-42.7.3.jar

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.3

RUN confluent-hub install --no-prompt debezium/debezium-connector-postgresql:latest