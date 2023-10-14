import random
import string
import psutil
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    len = 20
    lowerP = string.ascii_lowercase
    uppperP = string.ascii_uppercase
    digitsp = string.digits
    special_charac = string.punctuation
    combine = lowerP + uppperP + digitsp + special_charac
    x = random.sample(combine, len)
    passw = "".join(x)
    return f"Random Password: {passw}"


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')