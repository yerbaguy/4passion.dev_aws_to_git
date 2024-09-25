from flask import Flask, jsonify
import json
import requests



ewordable = Flask(__name__)

@ewordable.route('/', methods=['GET'])
def hello():
    return jsonify({"hello":"world"})

if __name__ == "__main__":

    ewordable.run(host='0.0.0.0', port=5000)
