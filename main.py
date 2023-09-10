from flask import Flask, jsonify, request
from datetime import datetime
import pytz
import os

app = Flask(__name__)
app.config['SECRET_key'] = os.environ.get('mariam')


@app.route('/')
def home():
    return jsonify(response='Hello world')


@app.route('/api')
def api():
    day = datetime.now(pytz.UTC).strftime('%A')
    time = datetime.now(pytz.UTC).strftime('%Y-%m-%dT%#H:%M:%SZ')
    
    return jsonify(slack_name=request.args.get('slack_name'),
                   current_day=day,
                   utc_time=time,
                   track=request.args.get('track'),
                   github_file_url='https://github.com/mayrhiarm/HNG-task/Taskone/main.py',
                   github_repo_url='https://github.com/HNG-task/Taskone',
                   status_code=200), 200


if __name__ == '__main__':
    app.run(debug=True)