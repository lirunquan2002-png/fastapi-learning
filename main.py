from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI 学习练习", version="0.1.0")


class Item(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    price: float = Field(gt=0)


@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/", status_code=201)
def create_item(item: Item):
    # 本课仅演示请求校验与响应，尚未连接数据库。
    return item


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
