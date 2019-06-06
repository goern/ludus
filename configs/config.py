# Configuration file for the application

datastore_configuration = {
    'type' : 'kafka'
}

kafka_configuration = {
    'bootstrap_server' : 'kafka.datahub.redhat.com:443',
    'cacert_file' : 'resources/data-hub-kafka-ca.crt',
    'topic' : 'dynamic-ludus-events-ingest-prod'
}

