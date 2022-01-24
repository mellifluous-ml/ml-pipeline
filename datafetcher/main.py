from fastapi import FastAPI
import os

app = FastAPI()

print(f"{os.getenv('SERVICE_NAME')} service.")
print(list(os.listdir(".")))
