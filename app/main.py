from fastapi import FastAPI

app = FastAPI()  # <-- Yeh "app" variable hona zaroori hai!

@app.get("/health")
def health_check():
    return {"status": "healthy"}