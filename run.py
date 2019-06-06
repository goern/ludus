from configs.config import datastore_configuration
from http import HTTPStatus
from flask import Flask, Response, request
from ludus.data_formatter import DataFormatter
from ludus.validator import Validator
from ludus.datastore import Datastore
import json

#constants
EVENT_SOURCE_GITHUB = "github"
EVENT_SOURCE_TRELLO = "trello"
STATUS_CODE_200 = HTTPStatus.OK
STATUS_CODE_500 = HTTPStatus.INTERNAL_SERVER_ERROR

#initializing datastore
datastore = Datastore.get_datastore(datastore_configuration['type'])

app = Flask(__name__)

@app.route('/github', methods=['POST'])
def github_event():

    resp = Response()
    event = request.json

    validator = Validator.get_validator(EVENT_SOURCE_GITHUB)
    is_valid, event_type  = validator.is_valid(event)

    if is_valid:
        data_formatter = DataFormatter.get_formatter(EVENT_SOURCE_GITHUB, event_type)
        formatted_event = data_formatter.format(event, event_type)
        formatted_event_json = json.dumps(formatted_event)

        try:
            datastore.insert(formatted_event_json.encode('utf-8'))
        except Exception as e:
            resp.status = "failed to insert event into datastore: "+ str(e)
            return resp, STATUS_CODE_500

    resp.status = "successfuly inserted event into datastore"
    return resp,STATUS_CODE_200


@app.route('/trello', methods=['POST', 'HEAD'])
def trello_event():

    resp = Response()
    event = request.json

    validator = Validator.get_validator(EVENT_SOURCE_TRELLO)
    is_valid, event_type = validator.is_valid(event)


    if is_valid:
        data_formatter = DataFormatter.get_formatter(EVENT_SOURCE_TRELLO, event_type)
        formatted_event = data_formatter.format(event, event_type)
        formatted_event_json = json.dumps(formatted_event)

        try:
            datastore.insert(formatted_event_json.encode('utf-8'))
        except Exception as e:
            resp.status = "failed to insert event into datastore: "+ str(e)
            return resp, STATUS_CODE_500

    resp.status = "successfuly inserted event into datastore"
    return resp, STATUS_CODE_200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

