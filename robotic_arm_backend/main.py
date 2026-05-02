from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.actions import router as actions_router

from routes.logs import router as logs_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(logs_router)

app.include_router(actions_router)


@app.get("/")
def root():
    return {"message": "Backend running "}