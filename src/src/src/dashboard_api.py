# dashboard_api.py

from flask import Flask, jsonify
from digital_twin_model import run_model

app = Flask(__name__)

@app.route('/api/status')
def get_status():
    status = run_model()
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True)
