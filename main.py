from fastapi import FastAPI
from database import Base, engine
import models.user
import models.document
import models.forms
import models.process
from routes import users
from routes import query
from routes import compliance




app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(query.router)
app.include_router(compliance.router)

@app.get("/")
def root():
    return {"message": "Environmental Licensing API is running"}

