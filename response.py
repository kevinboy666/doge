import requests
import json
from replit import db

#quotes
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
    db["encouragements"] = encouragements


def update_doges(doge_message):
    if "doges" in db.keys():
        doges = db["doges"]
        doges.append(doge_message)
        db["doges"] = doges
    else:
        db["doges"] = [doge_message]

def delete_doge(dmsg):
    doges = db["doges"]
    index = doges.index(dmsg) - 1
    #if len(doges) > index:
    del doges[index]
    db["doges"] = doges
