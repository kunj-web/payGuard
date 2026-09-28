from app.core.config import settings
from app.models.base import Base
import app.models  # noqa: F401  (import models so metadata is populated)

config.set_main_option("sqlalchemy.url", settings.database_url)
target_metadata = Base.metadata