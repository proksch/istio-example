from flask import Flask, Response
app = Flask(__name__)

VERSION = "0.0.1"
count = 0

@app.route('/', methods=['GET'])
def index():
    global count
    count += 1
    return {
        "version": VERSION
    }

@app.route('/metrics', methods=['GET'])
def metrics():
    global count

    m = "# HELP num_requests The number of requests that have been served.\n"
    m+= "# TYPE num_requests counter\n"
    m+= "num_requests{{fq_version=\"{}\"}} {}\n".format(VERSION, count)

    return Response(m, mimetype="text/plain")


app.run(host="0.0.0.0", port=8080, debug=True)