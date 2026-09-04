from fastapi import FastAPI

from api import router


def _init_router(app: FastAPI) -> None:
    app.include_router(router)


def server() -> FastAPI:
    app_ = FastAPI(title="Ecommerce API")
    _init_router(app_)

    return app_


app = server()
