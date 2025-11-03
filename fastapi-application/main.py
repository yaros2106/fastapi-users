from fastapi import FastAPI, Request

from fastapi.responses import ORJSONResponse

from app_lifespan import lifespan
from api import router as api_router


app = FastAPI(
    title="Example-Base-App",
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)


@app.get("/")
def read_root(request: Request) -> dict[str, str]:
    docs_url = request.url.replace(
        path="/docs",
        query="",
    )
    return {
        "docs": str(docs_url),
    }


app.include_router(api_router)
