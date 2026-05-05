from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import Base
import routers.books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Books API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.books.router)

@app.get("/")
def root():
    return {"message": "Books API is running"}
