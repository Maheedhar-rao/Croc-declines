from supabase import create_client, Client
import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Supabase credentials from .env file
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Initialize Flask app
app = Flask(__name__)
CORS(app)

def fetch_declines():
    try:
        response = supabase.table("declines").select("*").execute()
        if response.data:
            return response.data
        else:
            return []
    except Exception as e:
        return {"error": str(e)}

@app.route("/api/declines", methods=["GET"])
def get_deals():
    deals = fetch_declines()
    return jsonify(deals)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
