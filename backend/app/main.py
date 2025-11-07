from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routes import activities, auth, dashboard, deals, files, organizations, persons, pipelines, reports, tasks
from .core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.project_name)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.allowed_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth.router)
    app.include_router(organizations.router, prefix=settings.api_v1_prefix)
    app.include_router(persons.router, prefix=settings.api_v1_prefix)
    app.include_router(pipelines.router, prefix=settings.api_v1_prefix)
    app.include_router(deals.router, prefix=settings.api_v1_prefix)
    app.include_router(activities.router, prefix=settings.api_v1_prefix)
    app.include_router(tasks.router, prefix=settings.api_v1_prefix)
    app.include_router(files.router, prefix=settings.api_v1_prefix)
    app.include_router(reports.router, prefix=settings.api_v1_prefix)
    app.include_router(dashboard.router, prefix=settings.api_v1_prefix)

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
