from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#访问fastapi，响应：msg：你好Fastapi
@app.get("/user/{id}")
async def get_user(id: str,name:str):
    return {"id": f"{id}" , "name": f"{name}"}