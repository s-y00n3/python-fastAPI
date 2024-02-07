from typing import Annotated, List

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url:HttpUrl
    name:str
    
class Item(BaseModel):
    name: str
    #description: str | None = None
    description: str | None = Field(default=None, title="the description of the item", max_length=300),
    price : float = Field(gt=0, description="the price must be greater than zero")
    tax : float | None = None,
    #tags: List[str] = []
    tags: set[str] = set()
    #image: Image | None = None
    #images: list[Image] | None = None
    model_config = {
        "json_schema_extra" : {
            "examples" : [
                {
                    "name" : "foo",
                    "description" : "a nice item",
                    "price" : 24.5,
                    "tax" : 2.1
                }
            ]
        }
    }

class User(BaseModel):
    usernmae: str
    full_name: str | None = None


@app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="the id of the item to get", ge=0, le = 1000)],
#     q: str | None = None,
#     item: Item | None = None,
# ):
# if q:
#         results.update({"q" : q})
#     if item:
#         results.update({"item" : item})
#     return results

# importance : convert data types, validate, document
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id" : item_id, "item": item, "user" : user}
#     return results

# async def update_item(
#     item_id : int,
#     item: Item,
#     user: User,
#     importance: Annotated[int, Body(gt=0)],
#     q: str | None = None,
# ) :
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results

# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name":"foo",
                    "description" : "a very nice item!",
                    "price" : 25.4,
                    "tax" : 1.5,
                }
            ],
        ),
    ],
) :
    results = {"item_id" : item_id, "item" : item}
    return results