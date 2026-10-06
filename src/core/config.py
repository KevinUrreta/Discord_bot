from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    log_language: str = "en"

    discord_token: str
    youtube_oauth_refresh_token: str

    log_file: str = "./logs/bot.log"

    postgres_db: str = "postgres"
    postgres_user: str = "admin"
    postgres_password: str = "admin"
    postgres_host: str = "postgres"
    postgres_port: int = 5432

    lavalink_uri: str = "http://lavalink:2333"
    lavalink_password: str
    lavalink_port: int = 2333
    lavalink_opus: bool = True

    spotify_client_id: str
    spotify_secret_id: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
