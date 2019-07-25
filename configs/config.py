# Main configuration file for the application
from jinja2 import Environment, FileSystemLoader

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
    'faust_store': 'memory://',
    'events_table_name': 'aggregated_event_data_table_test_18',
    'badges_table_name': 'awarded_badges_table_test_18',
    'port' : 5001
}

formatter_configuration = {
    'jinja_environment' : Environment(loader=FileSystemLoader('formatters'))
}