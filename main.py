from fastapi import FastAPI
from routers import webhook
import uvicorn

app = FastAPI()

# Include your webhook router
app.include_router(webhook.router, prefix="/webhook")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
