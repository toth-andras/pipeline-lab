import os

from flask import Flask, jsonify

APP_VERSION = os.environ.get("APP_VERSION", "dev")

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(service="demo-app", version=APP_VERSION)


@app.get("/health")
def health():
    return jsonify(status="ok")
