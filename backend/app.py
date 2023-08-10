from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    subprocess.run(['python', 'leaderboard.py'])
    return 'Script executed successfully'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)  # Change port as needed