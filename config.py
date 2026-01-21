import os

DATABRICKS_HOST = os.getenv("DATABRICKS_HOST")
DATABRICKS_HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")

import os
from dotenv import load_dotenv

# Load .env from project root
load_dotenv(dotenv_path=".env")  # adjust path if your .env is somewhere else

DATABRICKS_HOST = os.getenv("DATABRICKS_HOST")
DATABRICKS_HTTP_PATH = os.getenv("DATABRICKS_HTTP_PATH")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")

print("HOST:", DATABRICKS_HOST)
print("HTTP_PATH:", DATABRICKS_HTTP_PATH)
print("TOKEN:", DATABRICKS_TOKEN)
