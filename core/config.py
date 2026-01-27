from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = (
    f"mysql+pymysql://{os.environ['DB_USER']}:"
    f"{os.environ['DB_PASS']}@"
    f"{os.environ['DB_HOST']}/"
    f"{os.environ['DB_NAME']}"
)