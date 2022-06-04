# http://127.0.0.1:8000/ -> adresse serveur
# rajouter /docs pour avoir acces au swagger
import re
import subprocess
from subprocess import Popen, PIPE
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from time import time
import httpx
import asyncio
import os
import ping3

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def request(client):
    response = await client.get("sfr.router")
    return response.text


async def task():
    async with httpx.AsyncClient() as client:
        tasks = [request(client) for i in range(1)]
        result = await asyncio.gather(*tasks)
        print(result)


@app.get('/')
async def f():
    # start = time()
    # await task()
    # print("time: ", time() - start)
    # hostname = "8.8.8.8"
    # response = os.system("ping -c 1 " + hostname)
    #
    # if response == 0:
    #     print(hostname, 'is up!')
    # else:
    #     print(hostname, 'is down!')
    # r = pyping.ping('google.com')
    #
    # if r.ret_code == 0:
    #     print("Success")
    # else:
    #     print("Failed with {}".format(r.ret_code))

    hostname = "192.168.1.1"
    process = subprocess.Popen(['ping', '-c', '1', hostname],
                               stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(stdout)
    ping_time = re.search('time=(.*) ms', stdout.decode('utf-8'))
    if ping_time is not None:
        ping_time = float(ping_time.group(1))
    # time = [x for x in stdout.decode('utf-8').split('\n') if x.find('time=') != -1][0].split('ms')[0]
    print("lel")
    print(ping_time)
    print("lol")
    packetloss = float(
        [x for x in stdout.decode('utf-8').split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
    print("Loss is %s percent" % packetloss)

    return {"Hello World"}


# @app.get("/")
# async def read_item():
#     print("damn son")
#
#     response = app.get("sfr.router")
#     print(response)
#     print("damn daughter")
#     return {"Hello World"}


# @app.post("/add")
# async def add():
#   d

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
