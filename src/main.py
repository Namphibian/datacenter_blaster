import logging
import uvicorn
from fastapi import FastAPI
import logging.config
from .system.logger import RouterLoggingMiddleware
from .system.logger_conf import logging_config
from .web import datacenter

logging.config.dictConfig(logging_config)
_LOGGER = logging.getLogger(__name__)
app = FastAPI(
    title="Datacenter Blaster API",
    version="0.0.1",
    debug=True,
    description="API to manage Datacenters and " "their associated network.",
)
app.add_middleware(RouterLoggingMiddleware, logger= _LOGGER)
app.include_router(datacenter.router)

_LOGGER.info("Starting uvicorn")
@app.get("/health", tags=["Health"])
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
