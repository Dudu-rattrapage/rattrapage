# http://127.0.0.1:8000/ -> adresse serveur
# rajouter /docs pour avoir acces au swagger
import re
import subprocess
from subprocess import Popen, PIPE
from types import SimpleNamespace

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ischedule import schedule, run_loop
import json

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open('data/entities.json') as file:
    # Parse JSON into an object with attributes corresponding to dict keys.
    entities = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))

print(entities.monitoring_delay)


def get_ping_infos_for_address():
    # beware since we access entities there is an intermittent spike?
    hostname = entities.entities[4].ip
    process = subprocess.Popen(['ping', '-c', '1', hostname],
                               stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()

    # invariant: assume it's always displaying milliseconds
    ping_time = re.search('time=(.*) ms', stdout.decode('utf-8'))
    if ping_time is not None:
        ping_time = float(ping_time.group(1))

    packetloss = float(
        [x for x in stdout.decode('utf-8').split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])

    if packetloss > 0.0:
        has_packet_loss = True
    else:
        has_packet_loss = False
    print(ping_time)
    # return [ping_time, has_packet_loss]


# dezoom
# https://pypi.org/project/ischedule/
# see also https://pypi.org/project/schedule/
# fixme replace 2 with var
schedule(get_ping_infos_for_address, interval=2)
run_loop()


# fixme: check ping windows support
@app.get('/')
async def get_ping_infos():
    # [ping_time, has_packet_loss] = get_ping_infos_for_address("8.8.8.8")
    # print(ping_time)
    # print(has_packet_loss)
    return {"Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
