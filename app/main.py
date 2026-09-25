from fastapi import FastAPI


app = FastAPI(
    title="Secure CI Pipeline Mini",
    version="1.0.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Secure CI Pipeline Mini",
        "status": "ok",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        #"status": "broken",
    }