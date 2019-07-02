# Main configuration file for the application

datastore_configuration = {
    'type' : 'kafka'
}

kafka_configuration = {
    'bootstrap_server' : 'kafka.datahub.redhat.com:443',
    'cacert_file' : 'resources/data-hub-kafka-ca.crt',
    'topic' : 'dynamic-ludus-events-ingest-prod'
}

awarder_configuration = {
    'faust_app_name': 'ludus_awarder',
    'events_table_name': 'aggregated_event_data_table_test_14',
    'badges_table_name': 'awarded_badges_table_test_14',
    'port' : 5001
}
