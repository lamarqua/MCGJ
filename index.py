from flask import Flask
from database import print_records

app = Flask(__name__)

@app.route('/')
def print_tracks():
    return print_records('tracks')