from typing import Dict

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Weblinks"


@app.route("/basic_hook", methods=["POST"])  # type: ignore
def basic_hook():
    data: Dict | None = request.json  # type: ignore
    if data is None:
        print("No Data")
        return "No Data"
    for key, value in data.items():
        print(f"{key}: {value}")
        return "OK"


if __name__ == "__main__":
    app.run(debug=True)
