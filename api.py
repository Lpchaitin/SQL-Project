import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

# Fetch the page
url = "https://www.baseball-reference.com/leagues/MLB-standings.shtml"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Grab all HTML tables
tables = soup.find_all("table")

# Initialize list to hold data
dfs = []

for table in tables:
    html_str = str(table)
    df = pd.read_html(StringIO(html_str))[0]  # <— this avoids the FutureWarning
    dfs.append(df)

# Combine and preview
combined_df = pd.concat(dfs, ignore_index=True)
combined_df.to_csv("mlb_standings.csv", index=False)
print(combined_df.head())

