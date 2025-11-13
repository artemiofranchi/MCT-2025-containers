import asyncpg
import os

DB_CONN = None

async def get_db():
    global DB_CONN
    if DB_CONN is None:
        DB_CONN = await asyncpg.connect(
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            database=os.getenv("POSTGRES_DB"),
            host="db"
        )
    return DB_CONN