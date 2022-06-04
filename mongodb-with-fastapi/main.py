#http://127.0.0.1:8000/ -> adresse serveur 
#rajouter /docs pour avoir acces au swagger
from fastapi import FastAPI,HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
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

@app.post("/add")
async def add():
  d

@app.get("/items/{item_id}")
async def read_item(item_id):
  return {"item_id": item_id}