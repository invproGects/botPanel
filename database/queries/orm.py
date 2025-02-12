from sqlalchemy import insert, select, delete, text

from database.database import async_session_factory, async_engine, sync_engine, Base
from database.models import UsersOrm


class AsyncORM:
	@staticmethod
	async def add_user(tgid: int):
		async with async_session_factory() as session:
			user = UsersOrm(tgid = tgid)

			session.add(user)

			await session.commit()

	@staticmethod
	async def get_user(tgID: int):
		async with async_session_factory() as session:
			users = await session.execute(select(UsersOrm).where(UsersOrm.tgid == tgID))
		return users.scalars().all()
	
	@staticmethod
	async def get_all_users():
		async with async_session_factory() as session:
			query = select(UsersOrm)
			result = await session.execute(query)

			users = result.all()
		return users
			
	@staticmethod
	async def update_user(tgig: int, **data):
		pass