from ludus.kafka_datastore import KafkaDatastore

class Datastore:
    def get_datastore(type):
        if type == 'kafka':
            return KafkaDatastore()

