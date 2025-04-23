from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

app = Flask(__name__)

http://127.0.0.1:5000/api/mlb-standings
def get_mlb_standings():
    url = "https://www.teamrankings.com/mlb/standings/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the standings table
    table = soup.find("table", {"class": "tr-table datatable scrollable"})
    if not table:
        return jsonify({"error": "Standings table not found"}), 404

    # Read the table into a DataFrame
    df = pd.read_html(StringIO(str(table)))[0]

    # Convert DataFrame to JSON
    standings = df.to_dict(orient='records')
    return jsonify(standings)

if __name__ == '__main__':
    app.run(debug=True)