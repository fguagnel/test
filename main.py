from fastapi import FastAPI

app = FastAPI()

# http://localhost:8000/hello
@app.get("/hello")
async def hello():
    return {"Hello": "World"}
