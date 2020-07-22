from fastapi import FastAPI
from starlette.responses import PlainTextResponse


app = FastAPI()

@app.get("/")
async def read_root():
    return PlainTextResponse(b'hello world')
