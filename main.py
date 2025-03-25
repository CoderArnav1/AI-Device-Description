import uvicorn
from fastapi import FastAPI
from routes.device_routes import router
from config.settings import HOST, PORT

app = FastAPI(title="Device Description API")

app.include_router(router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Welcome to the Device Description API"}

if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT, reload=True)

