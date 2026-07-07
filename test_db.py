from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print("DATABASE_URL =", DATABASE_URL)

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ Kết nối thành công!")
except Exception as e:
    print("❌ Lỗi:")
    print(e)