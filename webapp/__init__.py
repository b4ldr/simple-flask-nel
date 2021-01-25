import json

from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def root():
    return "nel collector!"


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    nel_packet = request.json
    nel_packet['client_ip'] = request.remote_addr
    app.logger.info(json.dumps(nel_packet, indent=2, sort_keys=True))
    return str(request.json)

if __name__ == "__main__":
    app.run()
