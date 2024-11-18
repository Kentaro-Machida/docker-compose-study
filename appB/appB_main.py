from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    env_var = os.getenv('ENV_VAR', 'ENV_VAR not set')
    text = f"Hello World this is appB. The value of the environment variable ENV_VAR is: {env_var}"
    return text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
