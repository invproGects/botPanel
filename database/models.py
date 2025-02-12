from sqlalchemy import Column, MetaData, Integer, String, Table, BigInteger, func, text
from sqlalchemy.orm import Mapped, mapped_column

from typing import Annotated
from datetime import datetime
from enum import Enum

from database.database import Base


class Roles(Enum):
	user = "user"
	admin = "admin"


registered_at = Annotated[datetime, mapped_column(server_default = text("TIMEZONE('utc', now())"))]

class UsersOrm(Base):
	__tablename__ = "users"

	tgid: Mapped[int] = mapped_column(BigInteger, primary_key = True, autoincrement = False)
	role: Mapped[Roles] = mapped_column(default = Roles.user)
	registered_at: Mapped[registered_at]
