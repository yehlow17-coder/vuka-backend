from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import version, announcements, configs, countries, health, networks
from app.config.settings import get_settings
from app.database.session import init_db

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version='1.0.0',
    description='VUKA backend for VPN config management.',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(health)
app.include_router(configs)
app.include_router(countries)
app.include_router(networks)
app.include_router(announcements)
app.include_router(version)


@app.on_event('startup')
async def on_startup() -> None:
    await init_db()


@app.get('/')
async def root() -> dict[str, str]:
    return {'message': 'VUKA backend is running.'}
