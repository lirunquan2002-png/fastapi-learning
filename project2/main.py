from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "515"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
