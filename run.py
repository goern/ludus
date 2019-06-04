from http import HTTPStatus
from flask import Flask, Response, request
from ludus.data_formatter import DataFormatter
from ludus.validator import Validator
import json

#constants
EVENT_SOURCE_GITHUB = "github"
EVENT_SOURCE_TRELLO = "trello"


app = Flask(__name__)

@app.route('/github', methods=['POST'])
def github_event():

    resp = Response()
    status_code = HTTPStatus.OK
    event = request.json

    validator = Validator.get_validator(EVENT_SOURCE_GITHUB)
    is_valid, event_type  = validator.is_valid(event)

    #print(is_valid)

    if is_valid:
        data_formatter = DataFormatter.get_formatter(EVENT_SOURCE_GITHUB, event_type)
        formatted_event = data_formatter.format(event, event_type)
        formatted_event_json = json.dumps(formatted_event)
        #print(formatted_event_json)

    return resp,status_code


@app.route('/trello', methods=['POST', 'HEAD'])
def trello_event():

    resp = Response()
    status_code = HTTPStatus.OK
    event = request.json

    validator = Validator.get_validator(EVENT_SOURCE_TRELLO)
    is_valid, event_type = validator.is_valid(event)

    #print(is_valid)

    if is_valid:
        data_formatter = DataFormatter.get_formatter(EVENT_SOURCE_TRELLO, event_type)
        formatted_event = data_formatter.format(event, event_type)
        formatted_event_json = json.dumps(formatted_event)
        #print(formatted_event_json)

    return resp, status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)