from core.session import database_helper
from db_models.base import Base
from db_models.User import User
import asyncio

async def create_table():
    async with database_helper.engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)
    await database_helper.dispose()


asyncio.run(create_table())
