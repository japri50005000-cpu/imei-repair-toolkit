# build d1aa312e6a
# (auto) ce1c07
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'ok'
