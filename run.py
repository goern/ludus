from http import HTTPStatus
from flask import Flask, Response, request
from ludus.data_formatter import DataFormatter
from ludus.validator import Validator

#constants
EVENT_SOURCE_GITHUB = "github"
EVENT_SOURCE_TRELLO = "trello"


app = Flask(__name__)

@app.route('/github', methods=['POST'])
def github_event():
    resp = Response()
    payload = None
    status_code = HTTPStatus.OK

    data = request.json

    validator = Validator.get_validator(EVENT_SOURCE_GITHUB)

    is_valid = validator.is_valid(data)

    print(is_valid)

    #formatted_data_json = DataFormatter.format(data, EVENT_SOURCE_GITHUB)

    #print(formatted_data_json)

    return resp,status_code


@app.route('/trello', methods=['POST', 'HEAD'])
def trello_event():
    resp = Response()
    payload = None
    status_code = HTTPStatus.OK

    data = request.json

    validator = Validator.get_validator(EVENT_SOURCE_TRELLO)

    is_valid = validator.is_valid(data)

    print(is_valid)

    #formatted_data_json = DataFormatter.format(data, EVENT_SOURCE_TRELLO)

    #print(formatted_data_json)

    return resp, status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)