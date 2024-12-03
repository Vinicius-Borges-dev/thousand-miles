from waitress import serve
from src import create_app
from dotenv import load_dotenv

load_dotenv('.env')
app = create_app()

if __name__ == "__main__":
    serve(app, host="localhost", port=8000)
