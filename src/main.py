import logging

from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from system.constants import static_dir
from system.db_connect import SessionLocal
from system.jinja import jinja
from system.logger import RouterLoggingMiddleware
from web import datacenter


_LOGGER = logging.getLogger(__name__)
app = FastAPI(
    title="Datacenter Blaster API",
    version="0.0.1",
    debug=True,
    description="API to manage Datacenters and their associated network.",
)

app.add_middleware(RouterLoggingMiddleware, logger=logging.getLogger(__name__))
app.include_router(datacenter.router)
app.mount("/static", StaticFiles(directory=static_dir), name="static")
_LOGGER.info("Starting uvicorn")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health", tags=["Health"])
def root():
    return {"message": "Hello World"}


@app.get("/")
@jinja.page("index.html")
def index() -> None:
    """This route serves the index.html template."""
    ...
# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
