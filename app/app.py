from typing import Dict

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Weblinks"


@app.route("/generic_hook", methods=["POST"])
def generic_hook() -> Dict[str, str]:
    data: Dict = request.get_json() or {}
    for key, value in data.items():
        print(f"{key}: {value}")
    return data


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
