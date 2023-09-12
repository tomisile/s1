from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/endpoint', methods=['GET'])
def api_endpoint():
    # Get query parameters from the request
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Check if both query parameters are provided
    if not slack_name or not track:
        return jsonify(error='Both slack_name and track parameters are required.'), 400

    # Your logic here to process the parameters
    # For this example, we'll simply return a JSON response
    response_data = {
        "slack_name": "tomistark",
        "current_day": "Tuesday",
        "utc_time": "2023-09-12T22:30:05Z",
        "track": "backend",
        "github_file_url": "https://github.com/tomisile/s1/blob/main/app.py",
        "github_repo_url": "https://github.com/tomisile/s1",
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
