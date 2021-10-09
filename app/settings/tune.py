from fastapi.middleware.cors import CORSMiddleware

from app.modules.history.routes import history_router
from app.modules.link_shorter.routes import short_router


def tune_routers(app):
    app.include_router(router=short_router, tags=['link_shorter'], prefix='/short')
    app.include_router(router=history_router, tags=['history'], prefix='/history')


def tune_cors(app):
    origins = [
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
