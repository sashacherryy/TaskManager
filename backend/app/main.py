from fastapi import FastAPI;
from app.db.database import Base, engine
from app.routers.tasks import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, tags=["tasks"])

@app.get("/")
async def healt_check():
    return {"status": "ok"}