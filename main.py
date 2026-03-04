from fastapi import FastAPI

app = FastAPI(title="Fastapi CI/CD demo")

async def root():
    return {"message": "FastAPI CI/CD working 🚀"}