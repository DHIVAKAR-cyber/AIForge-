
from fastapi import FastAPI

app = FastAPI(
    title="AIForge",
    description="AETHER-X Intelligent AI Infrastructure",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to AIForge",
        "project": "AETHER-X",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "aiforge",
        "version": "0.1.0"
    }
