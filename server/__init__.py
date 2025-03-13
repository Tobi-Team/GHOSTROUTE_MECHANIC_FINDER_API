"""
Copyright (c) 12/2024 - iyanuajimobi12@gmail.com
"""

import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from .config import init_db, app_configs
from .controllers import router


def create_app(app_name: str = 'Mechanic Finder') -> FastAPI:
    """
    The create_app function is the entry point for our application.
    """

    # inject global dependencies
    app = FastAPI(
        title=app_name.capitalize(),
        description=f'{app_name.capitalize()}`s Api Documentation',
        docs_url='/api/docs',
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_configs.CORS_ALLOWED,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/", include_in_schema=False)
    def redirect():
        return RedirectResponse(url='/api/docs', status_code=302)

    @app.get("/status")
    def status():
        return {"status": "running"}

    @app.exception_handler(404)
    async def not_found_404(request, exc):
        return RedirectResponse(url='/api/docs', status_code=302)

    app.include_router(router)
    init_db()
    return app
