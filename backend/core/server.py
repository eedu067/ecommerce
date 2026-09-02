from fastapi import FastAPI


def server() -> FastAPI:
    app_ = FastAPI(title="Ecommerce API")

    return app_


app = server()
