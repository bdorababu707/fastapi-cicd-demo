from fastapi import FastAPI

app = FastAPI(title="Fastapi CI/CD demo")

@app.get("/")
async def root():
    return {"message": "FastAPI CI/CD working 🚀"}