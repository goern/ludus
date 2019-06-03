from http import HTTPStatus
from flask import Flask, Response, request
import json

app = Flask(__name__)


@app.route('/github', methods=['POST'])
def github_event():
    resp = Response()
    payload = None
    status_code = HTTPStatus.OK

    content = request.json
    print(json.dumps(content))

    return resp,status_code


@app.route('/trello', methods=['POST', 'HEAD'])
def trello_event():
    resp = Response()
    payload = None
    status_code = HTTPStatus.OK

    content = request.json
    print(json.dumps(content))

    return resp, status_code