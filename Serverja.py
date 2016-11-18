from flask import Flask
from libi import libardrone
app = Flask(__name__)
libardrone = libardrone()
@app.route('/')
def index():
    libardrone.takeoff
    return 'Binpaileoy !'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
