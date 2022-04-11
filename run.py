from config import HOST, PORT, DEBUG
from app import app

app.run(host = HOST, port = PORT, debug = DEBUG)