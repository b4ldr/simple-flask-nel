from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def root():
    return "nel collector!"


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    app.logger.info(request.json)
    return str(request.json)

if __name__ == "__main__":
    app.run()
