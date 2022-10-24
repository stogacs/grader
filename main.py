from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from waitress import serve
import logging
import api
import asyncio

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask('')
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)


@app.route('/')
async def home():
    return "sup"


@app.route("/getLanguages", methods=["GET"])
async def getLanguages():
    response = jsonify(await api.getLanguages())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/execute", methods=["POST"])
async def execute():
    lang = request.form["lang"]
    code = request.form["code"]
    input = request.form["inputs"]
    return jsonify(await api.execute(code, lang, input))


@app.route("/submit", methods=["POST"])
async def submit():
    lang = request.form["lang"]
    code = request.form["code"]
    problem = request.form["problem"]

    res = []

    for i in range(9):
        with open(f"p{problem}/in{i+1}.txt") as f:
            input = f.read()
        out = await api.getOutput(code, lang, input)
        out = out.strip()
        with open(f"p{problem}/out{i+1}.txt") as f:
            output = f.read().strip()

        res.append(output == out)

    response = jsonify(res)
    return response


async def run():
    serve(app, host="0.0.0.0", port=8080)


loop = asyncio.new_event_loop()
loop.run_until_complete(run())
