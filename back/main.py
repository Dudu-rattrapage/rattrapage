#http://127.0.0.1:8000/ -> adresse serveur 
#rajouter /docs pour avoir acces au swagger
from fastapi import FastAPI,HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_item():
    return {"Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id):
  return {"item_id": item_id}


def insertValues(TimeStamp,Ip,Domain,Description,Ping,PacketLoss):
    conn = sqlite3.connect('BDD/rattrapage.db')
    c = conn.cursor()
    data = (TimeStamp, Ip, Domain, Description, Ping, PacketLoss)
    c.execute("INSERT INTO ping_request_results (TimeStamp, IP, Domain, Description, Ping, PacketLoss) VALUES (?,?,?,?,?,?);"
    ,data)
    print("Values insert sucessfuly")
    conn.commit()
    conn.close()

def getAll():
    conn = sqlite3.connect('BDD/rattrapage.db')
    c = conn.cursor()
    c.execute("SELECT * FROM ping_request_results")
    list = c.fetchall()
    conn.commit()
    conn.close()
    print(list)
    return list

