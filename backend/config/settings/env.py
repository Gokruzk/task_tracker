from os import getenv
from dotenv import load_dotenv

load_dotenv()


class ServerConfig:
    @staticmethod
    def port() -> int:
        return int(getenv("PORT") or 8000)

    @staticmethod
    def environment() -> str:
        return getenv("ENVIRONMENT") or "production"


class DBConfig:
    @staticmethod
    def name() -> str:
        return getenv("DATABASE_DB_NAME") or getenv("DB_NAME")

    @staticmethod
    def user() -> str:
        return getenv("DATABASE_DB_USER") or getenv("DB_USER")

    @staticmethod
    def psw() -> str:
        return getenv("DATABASE_DB_PSW") or getenv("DB_PSW")

    @staticmethod
    def port() -> str:
        return getenv("DATABASE_DB_PORT") or "5432"

    @staticmethod
    def host() -> str:
        return getenv("DATABASE_DB_HOST") or "db"


class JWTConfig:
    @staticmethod
    def algorithm() -> str:
        return getenv("ALGORITHM") or "HS256"

    @staticmethod
    def secret_key() -> str:
        return getenv("SECRET_KEY") or ""

    @staticmethod
    def token_expire() -> int:
        return int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or 120)
