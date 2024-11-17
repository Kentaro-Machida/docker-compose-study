from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello_world():
    test = np.random.randint(0, 100)
    return f"Hello World this is app1 and the random number is: {test}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
