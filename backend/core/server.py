from typing import List

from fastapi import FastAPI
from fastapi.middleware import Middleware

from api import router
from core.middlewares import AuthBackend, AuthenticationMiddleware


def _init_router(app: FastAPI) -> None:
    app.include_router(router)


def make_middleware() -> List[Middleware]:
    middlewares = [Middleware(AuthenticationMiddleware, backend=AuthBackend())]
    return middlewares


def server() -> FastAPI:
    app_ = FastAPI(title="Ecommerce API", middleware=make_middleware())
    _init_router(app_)

    return app_


app = server()
