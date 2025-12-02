from fastapi import FastAPI
import uvicorn

from controllers import user_router, post_router

app = FastAPI(title="JWT Users-Posts", version="0.0.1")

app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(post_router, prefix="/api", tags=["posts"])

@app.get("/")
def root():
    return {
        "status": 200,
        "success": True,
        "message": "The server is working"
    }

@app.get("/api/health")
def health():
    return {
        "status": 200,
        "success": True,
        "message": "The server is healthy"
    }

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)