# http://127.0.0.1:8000/ -> adresse serveur
# rajouter /docs pour avoir acces au swagger
import copy
import re
import subprocess
import time
from subprocess import Popen, PIPE
from types import SimpleNamespace

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ischedule import schedule, run_loop
import json
import sqlite3

from BDD.init import initialize_db_tables, reset_database
from fastapi_utils.tasks import repeat_every

app = FastAPI()

# initialize_db_tables()
# reset_database()
initialize_db_tables()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def insertValues(TimeStamp, Ip, Domain, Description, Ping, PacketLoss):
    conn = sqlite3.connect('rattrapage.db')
    c = conn.cursor()
    data = (time.strftime('%Y-%m-%d %H:%M:%S'), Ip, Domain, Description, Ping, PacketLoss)
    c.execute(
        "INSERT INTO ping_request_results (TimeStamp, IP, Domain, Description, Ping, PacketLoss) VALUES (?,?,?,?,?,?);"
        , data)
    print("Values insert sucessfuly")
    conn.commit()
    conn.close()


def getAll():
    conn = sqlite3.connect('rattrapage.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ping_request_results")
    list = c.fetchall()
    conn.commit()
    conn.close()
    # print(list)
    return list


with open('data/entities.json') as file:
    # Parse JSON into an object with attributes corresponding to dict keys.
    entities_obj = json.loads(file.read(), object_hook=lambda d: SimpleNamespace(**d))

print(entities_obj.monitoring_delay)


def insert_ping_infos_for_entity(entity: any):
    hostname = entity.ip
    # beware since we access entities there is an intermittent spike?
    # todo windows support: https://stackoverflow.com/questions/2953462/pinging-servers-in-python
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
    insertValues("hoho", entity.ip, entity.domain, entity.description, ping_time, has_packet_loss)


# async??
# https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/
@app.on_event("startup")
@repeat_every(seconds=entities_obj.monitoring_delay)
def insert_ping_infos_for_each_address():
    entities = entities_obj.entities
    for entity in entities:
        insert_ping_infos_for_entity(entity)

    print("wow")
    # return [ping_time, has_packet_loss]


def get_ping_infos_for_each_address():
    entities = entities_obj.entities

    response = copy.deepcopy(entities)
    for entity in response:
        entity.ping_metadata = []
        # nullable members
        entity.pings = []
        entity.has_packet_loss = []
        entity.timestamps = []

    results = getAll()
    for entity in response:
        for result in results:
            # if domains match
            if result[2] == entity.domain:
                entity.ping_metadata.append(result)
        # sort by time
        entity.ping_metadata.sort(key=lambda x: time.mktime(time.strptime(x[0], '%Y-%m-%d %H:%M:%S')))
        for column in entity.ping_metadata:
            entity.timestamps.append(column[0])
            entity.pings.append(column[4])
            entity.has_packet_loss.append(column[5])

    print("damn son")
    print(response[0].timestamps)
    return response


# https://pypi.org/project/ischedule/
# see also https://pypi.org/project/schedule/
# schedule(insert_ping_infos_for_each_address, interval=entities_obj.monitoring_delay)
# run_loop()


# fixme: check ping windows support
@app.get('/')
async def get_ping_infos():
    # [ping_time, has_packet_loss] = get_ping_infos_for_address("8.8.8.8")
    # print(ping_time)
    # print(has_packet_loss)
    print("damn thats a testtt")

    return get_ping_infos_for_each_address()
    # return {"lol": "hehe"}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
