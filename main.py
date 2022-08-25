import logging
from typing import Union
import requests
from fastapi import FastAPI
from pydantic import BaseModel # adicionar en los imports en el main.py
from uicheckapp import EchoService

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    url = 'https://62f7c505ab9f1f8e89030fc1.mockapi.io/items'
    response = requests.get(url, {}, timeout=5)
    return {"items": response.json() }

@app.get("/item")
def read_root():
    return [{"id": "1"}, {"id": "2"}]

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    url = 'https://62f7c505ab9f1f8e89030fc1.mockapi.io/items'
    response = requests.get(url + '/' + str(item_id))
    #return {"item_id": item_id, "q": q}
    return {"items": response.json()}

@app.post("/items/")
def save_item(item: Item):
    url = 'https://62f7c505ab9f1f8e89030fc1.mockapi.io/items'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.post(url, item.json(), timeout = 5, headers = headers)
    return response.json()

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    url = 'https://62f7c505ab9f1f8e89030fc1.mockapi.io/items'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.put(url + "/" + str(item_id), item.json(), headers = headers)
    return response.json()
    #return {"item_name": item.name, "item_id": item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    url = 'https://62f7c505ab9f1f8e89030fc1.mockapi.io/items'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    response = requests.delete(url + "/" + str(item_id), headers = headers)
    return response.json()

# setup loggers
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  # the __name__ resolve to "main" since we are at the root of the project. 
                                      # This will get the root logger since no logger in the configuration has this name.

app = FastAPI()


@app.get("/")
async def root():
    logger.info("logging from the root logger")
    EchoService.echo("hi")
    return {"status": "alive"}
