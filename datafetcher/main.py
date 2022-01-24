import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
@app.get("/home")
def home():
    return {"message": "home"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=5000)
