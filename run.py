import os


if __name__ == "__main__":
    os.system("uvicorn app.main:app --port 8000 --reload")

    