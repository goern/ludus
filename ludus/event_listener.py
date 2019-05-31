from flask import Flask

app = Flask(__name__)


@app.route('/github', methods=['POST'])
def github_event():
    print('recieved a github event')
    return 'recieved a github event'


@app.route('/trello', methods=['POST', 'HEAD'])
def trello_event():
    print('received a trello event')
    return 'recieved a trello event'