from typing import Annotated
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
# async def read_items(
#     item_id : int = Path(title="the id of the item to get"),
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ) :

# 숫자 검증 (ge, gt, le, lt)
async def read_items(
    item_id: Annotated[int, Path(title="the id of the item to get", gt = 0, le = 1000)],
    q: str,
    size: float = Query(gt= 0, lt=10.5), # float 값에도 동작
):
    results = {"item_id" : item_id}
    if q:
        results.updatE({"q" : q})
    return results
    