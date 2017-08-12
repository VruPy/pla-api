from flask import request
from flask import make_response
from flask import Response
from flask import Flask
from flask import jsonify
app = Flask(__name__)
#import logging
#log = logging.basicConfig()

@app.route("/webhook",methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    #print type(req)
    res = processRequest(req)
    #name = req.get("result").get("parameters").get("name")
    #return Response(name)
    return make_response(jsonify(res))

def processRequest(req):

    if req.get("result").get("action") != "greetings":
        return {}

    name = req.get("result").get("parameters").get("name")
    #res  = make_webhook_response(name)
    return make_webhook_response(name)


def make_webhook_response(name):
    speech = "Hi "+name
    return {
        "displayText":speech,
        "speech":speech,
    }


if __name__ == "__main__":
    app.run(debug=True)