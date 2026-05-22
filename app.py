"""
Website Scraper – Flask Web Interface
Run this file to launch the web interface locally.
"""

from flask import Flask, request, jsonify, send_file, send_from_directory
import os, sys

# Make sure the scraper module is importable
sys.path.insert(0, os.path.dirname(__file__))
from scraper.scraper import run_scraper

app = Flask(__name__, static_folder="templates", static_url_path="")

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


@app.route("/")
def index():
    return send_from_directory("templates", "index.html")


@app.route("/api/scrape", methods=["POST"])
def scrape():
    data = request.get_json()
    url = data.get("url", "").strip()
    fields = data.get("fields", [])
    output_format = data.get("output_format", "csv")

    if not url:
        return jsonify({"error": "URL is required."}), 400
    if not fields:
        return jsonify({"error": "Select at least one data field."}), 400
    if output_format not in ("csv", "json", "excel"):
        return jsonify({"error": "Invalid output format."}), 400

    result = run_scraper(url, fields, output_format, OUTPUT_DIR)
    return jsonify(result)


@app.route("/api/download/<path:filename>")
def download(filename):
    return send_file(os.path.join(OUTPUT_DIR, filename), as_attachment=True)


if __name__ == "__main__":
    print("\n" + "="*50)
    print("  Website Scraper – Starting...")
    print("  Open your browser at: http://127.0.0.1:5000")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)
