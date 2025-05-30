from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

env_path = Path(__file__).resolve().parents[2] / '.env'

class Options(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path,
        extra='ignore',
        case_sensitive=False
    )
    local_dsn: PostgresDsn = Field(alias='ENGINE__LOCAL_DSN')
    password: str = Field(alias='POSTGRES_PASSWORD')
    user: str = Field(alias='POSTGRES_USER')
    db: str = Field(alias='POSTGRES_DB')


options = Options()
