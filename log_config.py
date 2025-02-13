from logging import (
	getLogger,
	basicConfig,
	Formatter,
	FileHandler,

	DEBUG,
	INFO,
	WARNING,
	ERROR,
	CRITICAL
)

from datetime import datetime
from datetime import timezone

basicConfig(
	level = INFO,
    format = "%(asctime)s | %(levelname)s | %(message)s",
	datefmt = r"%Y-%m-%d %H:%M:%S"
)

getLogger("aiogram").setLevel(WARNING)

bot_logger = getLogger("bot.messages")
bot_logger.setLevel(INFO)

_datetime = datetime.now(timezone.utc)
_date = _datetime.date()
_time = str(_datetime.time()).split(".")[0].replace(":", "-")

_filename = f"logs\\{_date}_{_time}.log"

_file_handler = FileHandler(_filename, encoding="utf-8")

_bot_formatter = Formatter(
	"%(asctime)s - %(message)s",
	datefmt = r"%Y-%m-%d %H:%M:%S"
)

_file_handler.setFormatter(_bot_formatter)

bot_logger.addHandler(_file_handler)