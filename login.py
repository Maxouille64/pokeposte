import sys
import json
import requests

from src.senders import sender

async def log_in(websocket, challid, chall):

    with open(sys.path[0] + "/src/id.txt") as logfile:
        username = logfile.readline()[:-1]
        password = logfile.readline()[:-1]
    resp = requests.post("https://play.pokemonshowdown.com/action.php?",
                         data={
                            'act': 'login',
                            'name': username,
                            'pass': password,
                            'challstr': challid + "%7C" + chall
                         })
    await sender(websocket, "", "/trn " + username + ",0," + json.loads(resp.text[1:])['assertion'])