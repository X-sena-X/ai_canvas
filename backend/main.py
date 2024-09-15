from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from constants import SERVER_URL, PORT, ENV
from router.route import router as calculate_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ai-canvas-frontend.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health_check():
    return {"message": "Server is running"}


app.include_router(calculate_router, prefix="/evaluate", tags=["evaluate"])


if __name__ == "__main__":
    uvicorn.run(app, host=SERVER_URL, port=PORT)
