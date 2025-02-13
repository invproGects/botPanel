from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine

from config import settings

async_engine = create_async_engine(
	settings.DATABASE_URL_asyncpg,
	echo = False
)

sync_engine = create_engine(
	settings.DATABASE_URL_psycopg,
	echo = False
)


async_session_factory = async_sessionmaker(async_engine)


class Base(DeclarativeBase):
	pass


def create_tables(recreation: bool = False):
	if recreation:
		Base.metadata.drop_all(sync_engine)
	Base.metadata.create_all(sync_engine)