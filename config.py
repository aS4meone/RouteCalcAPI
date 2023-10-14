from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("APIKEY")

DATABASE_URL = f"postgresql://postgres:mysecretpassword@localhost:5432/postgres"