from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import build, templates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(build.router, prefix="/api")
app.include_router(templates.router, prefix="/api")
