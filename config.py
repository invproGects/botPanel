from pydantic_settings import BaseSettings, SettingsConfigDict
from queue import Queue

class Settings(BaseSettings):
	DB_HOST: str
	DB_PORT: int
	DB_USER: str
	DB_PASS: str
	DB_NAME: str

	DB_ECHO: bool

	BOT_TOKEN: str

	OWNER_USERNAME: str
	APP_NAME: str

	@property
	def DATABASE_URL_asyncpg(self):
		return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
	
	@property
	def DATABASE_URL_psycopg(self):
		return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
	
	model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
log_queue = Queue()