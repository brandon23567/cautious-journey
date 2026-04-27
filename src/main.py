from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="None yet",
    description="This is just to test it with sveltekit and deploy them from there",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True
)


@app.get("/")
async def home_root():
    return { "message": "This is the base route for now" }