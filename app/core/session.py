from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine, AsyncSession
from core.options import options

class DatabaseHelper:
    def __init__(self, dsn: str):
        self.engine: AsyncEngine = create_async_engine(url=str(dsn))
        self.session_factory = async_sessionmaker(bind=self.engine, expire_on_commit=False, autoflush=False)
    async def dispose(self):
        await self.engine.dispose()
    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory as session:
            yield session

database_helper = DatabaseHelper(options.local_dsn)

# engine = create_async_engine(str(options.local_dsn))
# async_session_factory = async_sessionmaker(engine, expire_on_commit=False, autoflush=False)
#
#
# async def get_session():
#     async with async_session_factory as session:
#         yield session

