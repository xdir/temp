import subprocess
import random
import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/deploy', methods=['GET'])
def deploy():
    result = subprocess.run(['git', 'pull'], shell=True, text=True, capture_output=True)
    output = result.stdout
    print(output)
    if result.returncode != 0:
        return f"Error executing command: {result.stderr}", 500
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)