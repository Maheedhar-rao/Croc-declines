from fastapi import FastAPI
import os
from supabase import create_client

app = FastAPI()

SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_SECRET_KEY"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/api/declines")
def get_declines():
    response = supabase.table("declines").select("*").execute()
    return response.data
