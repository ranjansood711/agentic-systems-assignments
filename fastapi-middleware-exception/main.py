from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(">>> Before processing: Request received")
    print(f"HTTP Method: {request.method}")
    print(f"URL Path: {request.url.path}")

    response = await call_next(request)

    print("<<< After processing: Response returned\n")

    return response


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: 404):
    return JSONResponse(
        status_code=404,
        content={"message": "The requested resource was not found"}
    )


@app.get("/hello")
async def read_hello():
    return {
        "message": "Hello, Welcome to FastAPI!"
    }