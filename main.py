from fastapi import FastAPI
from database import Base, engine
import models.user
import models.document

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Environmental Licensing API is running"}