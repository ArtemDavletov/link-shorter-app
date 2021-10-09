import uvicorn as uvicorn
from fastapi import FastAPI

from app.settings import tune
from app.settings.database import Base, engine
from app.settings.settings import settings

Base.metadata.create_all(bind=engine)

app = FastAPI()

tune.tune_cors(app=app)
tune.tune_routers(app=app)


@app.get("/version")
def version():
    return "1.0.0"


if __name__ == '__main__':
    uvicorn.run(
        '__main__:app',
        host=settings.APP_HOST,
        reload=settings.DEBUG_MODE,
        port=settings.APP_PORT,
    )
