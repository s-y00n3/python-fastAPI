from typing import List, Union

from fastapi import FastAPI, Query
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class ModelName(str, Enum) :
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None) :
    return {"item_id" : item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item) :
    return {"item_name" : item.price, "item_id" : item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id" : "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str) :
    return {"user_id" : user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName) :
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep learning"}
    if model_name.value == "lenet":
        return {"model_name" : model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message" : "have some residuals"}

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# max_length, min_length : 쿼리 최대, 최소 길이 설정
# pattern : 정규식
@app.get("/items")
#async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50, pattern="^fixedquery&")):
#async def read_items(q: str = Query(default="fixedquery", min_lenth = 3)):

# 쿼리 매개변수 리스트 / 다중값
#async def read_items(q: Union[List[str], None] = Query(default=None)) : 

# 쿼리 다중값 기본값 설정
#async def read_items(q: List[str] = Query(default=["foo", "bar"])) :

# List[str] 대신 list 사용
#async def read_items(q: list = Query(default=[])):

# 메타데이터 선언
#async def read_items(q: Union[str, None] = Query(default=None, title="query string", description="description", min_length=3)) : 

# 별칭 매개변수
# deprecated = true로 설정하면 매개변수 사용되지 않음을 알림
async def read_items(q:Union[str, None] = Query(default=None, alias="item-query")) :
    results = {"items" : [{"item_id": "Foo"} , {"item_id" : "Bar"}]}
    if q:
        results.update({"q" : q})
    return results