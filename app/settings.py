import os

env = os.environ

DATABASE = {
    "DBHOST": env.get("DB_HOST") or "localhost",
    "DBPORT": env.get("DB_POST") or "5432",
    "DBUSER": env.get("DB_USER") or "postgres",
    "DBPASS": env.get("DB_PASS") or "",
    "DBNAME": env.get("DB_NAME") or "mydb"
}

SECRET_KEY = os.urandom(16)

DEFAULT_REDIRECT="auth/login"