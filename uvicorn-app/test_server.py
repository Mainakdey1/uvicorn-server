from fastapi import FastAPI
import asyncpg

app = FastAPI()


DB_CONFIG = {
    "user": "postgres",
    "password": "steprosis4.56", 
    "database": "indian_banks",
    "host": "localhost",
    "port": 5432
}


async def get_db():
    return await asyncpg.create_pool(**DB_CONFIG)

@app.get("/")
async def home():
    return {"message": "Indian Banks API is running!"}

@app.get("/banks")
async def get_banks():
    pool = await get_db()
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT * FROM banks;")
    return [dict(row) for row in rows]

@app.get("/branches/{ifsc}")
async def get_branch_by_ifsc(ifsc: str):
    pool = await get_db()
    async with pool.acquire() as conn:
        row = await conn.fetchrow("SELECT * FROM branches WHERE ifsc = $1;", ifsc)
    return dict(row) if row else {"error": "Branch not found"}


