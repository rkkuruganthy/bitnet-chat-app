# api_server.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from bitnet_runner import run_bitnet

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 200

@app.post("/generate")
def generate(req: PromptRequest):
    response = run_bitnet(req.prompt, req.max_tokens)
    return {"response": response}
