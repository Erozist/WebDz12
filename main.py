from fastapi import FastAPI
from src.database.db import engine, Base
from src.routes import contacts, auth

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(auth.router)
app.include_router(contacts.router)
