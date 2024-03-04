import os
from dotenv import load_dotenv
load_dotenv()
list_env_var = [
    os.environ.get("DB_HOST"),
    os.environ.get("DB_USER"),
    os.environ.get("DB_PASS"),
    os.environ.get("DB_NAME"),
    os.environ.get("DB_PORT"),
    
]

for item in list_env_var:
    print(item)