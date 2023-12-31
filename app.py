from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-data', methods=['GET'])
def get_data():
    # Replace with your private API URL and required headers
    api_url = 'https://web3api.io/api/v2/market/exchanges'
    headers = {
        'x-api-key': 'UAK5b2464bd90aa63316784d05427a042f7',  # Replace with your API token
        'accept': 'application/json'
        # Include other necessary headers
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        data = response.json()

        # Extracting the exchange names
        exchange_names = list(data.get('payload', {}).get('data', {}).keys())

        return jsonify(exchange_names)
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(port=5001)
