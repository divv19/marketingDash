# app.py
from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# --- Configuration ---
# Define the path to the data directory relative to the app.py file
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')

# --- Routes ---
# Route to serve the main dashboard page (index.html)
@app.route("/")
def index():
    """
    Route for the root URL ("/").
    Renders the index.html template to display the dashboard.
    """
    return render_template('index.html')

# API endpoint to serve market share data
@app.route("/api/marketShare")
def get_market_share():
    """
    API endpoint for "/api/marketShare".
    Reads data from marketShare.json and returns it as JSON.
    """
    try:
        filepath = os.path.join(DATA_DIR, 'marketShare.json')
        with open(filepath, 'r') as f:
            market_share_data = json.load(f)
        return jsonify(market_share_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

# API endpoint to serve revenue trends data
@app.route("/api/revenueTrends")
def get_revenue_trends():
    """
    API endpoint for "/api/revenueTrends".
    Reads data from revenueTrends.json and returns it as JSON.
    """
    try:
        filepath = os.path.join(DATA_DIR, 'revenueTrends.json')
        with open(filepath, 'r') as f:
            revenue_trends_data = json.load(f)
        return jsonify(revenue_trends_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

# API endpoint to serve market segmentation data
@app.route("/api/marketSegmentation")
def get_market_segmentation():
    """
    API endpoint for "/api/marketSegmentation".
    Reads data from marketSegmentation.json and returns it as JSON.
    """
    try:
        filepath = os.path.join(DATA_DIR, 'marketSegmentation.json')
        with open(filepath, 'r') as f:
            market_segmentation_data = json.load(f)
        return jsonify(market_segmentation_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format in data file"}), 500

# --- Static Files ---
# Flask automatically serves static files from the 'static' folder in the same directory as app.py.
# No explicit route configuration needed for static files in this case if using default 'static' folder.
# If you need to serve from a different folder or with a different URL, you would configure app.static_folder and app.static_url_path.

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True) # Set debug=False for production
