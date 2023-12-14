from flask import Flask, request

app = Flask(__name__)

@app.route('/alkuluku/31')

def alkuluku():
    args = request.args

    alkuluku = 31

    for jakaja in range(2, int(alkuluku**0.5) + 1):
        if alkuluku % jakaja == 0:
            alkuluku = False

    vastaus = {
        "Number": alkuluku,
        "isPrime": True
    }

    return vastaus


