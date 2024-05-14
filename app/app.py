from flask import Flask, Response
import requests
from os import environ

app = Flask(__name__)

VERSION = "0.0.2"
count = 0

def request_lib_version(url):
    res = requests.get(url)
    try:
        return res.json()["version"]
    except:
        return "uparseable: " + str(res)

@app.route('/', methods=['GET'])
def index():
    global count
    count += 1

    if not "LIB_URL" in environ:
        return "Error: LIB_URL not set in environment"

    res = request_lib_version(environ["LIB_URL"])

    return {
        "lib": res,
        "app": VERSION
    }

@app.route('/metrics', methods=['GET'])
def metrics():
    global count

    m = "# HELP num_requests The number of requests that have been served.\n"
    m+= "# TYPE num_requests counter\n"
    m+= "num_requests{{fq_version=\"{}\"}} {}\n".format(VERSION, count)

    return Response(m, mimetype="text/plain")

app.run(host="0.0.0.0", port=8080, debug=True)