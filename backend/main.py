import uvicorn

from core.config import EnvEnum, config

if __name__ == "__main__":
    uvicorn.run(
        "core.server:app",
        port=config.PORT,
        host=config.HOST,
        reload=config.ENVIRONMENT == EnvEnum.DEVELOPMENT,
    )
