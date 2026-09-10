from fastapi import FastAPI,Path

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#访问fastapi，响应：msg：你好Fastapi
@app.get("/user/{id}")
async def get_user(id: int=Path(...,gt=0,lt=101,description="书籍id，取值范围1-100")):
    return {"id": f"{id}" ,"tltle":"这是第{id}本书"}


#需求：查找书籍的作者，路径参数name，长度范围2-10
@app.get("/booker/{name}")
async def get_booker(name:str = Path(...,min_length=2,max_length=4)):
    return {"msg":f"这是{name}的信息"}