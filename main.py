from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import chat, suggested_questions, text_to_speech

from routes import authentication


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(text_to_speech.router)
app.include_router(authentication.router)
app.include_router(suggested_questions.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
