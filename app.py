from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get-data', methods=['GET'])
def get_data():
    # Replace with your private API URL and required headers
    api_url = 'https://your-private-api.com/data'
    headers = {
        'Authorization': 'Bearer YOUR_API_TOKEN', # Replace with your API token
        # Include other necessary headers
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
