from fastapi import FastAPI
from routes import webhook


app = FastAPI()


app.include_router(webhook.router)
