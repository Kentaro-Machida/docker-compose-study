from flask import Flask
import numpy as np
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    test = np.random.randint(0, 10000)
    env_var = os.getenv('ENV_VAR', 'ENV_VAR not set')
    text = f"Hello World this is appA and the random number is: {test}. The value of the environment variable ENV_VAR is: {env_var}. Working dir:{os.getcwd()}"
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
