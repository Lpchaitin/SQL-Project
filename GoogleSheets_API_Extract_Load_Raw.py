import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and authenticate with the service account
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("/workspaces/SQL-Project/mlb-data-collection-457705-5341e1a51e0b.json", scope)  # Correct path to your credentials file
client = gspread.authorize(creds)

# Open the Google Sheet by its URL
sheet_url = "https://docs.google.com/spreadsheets/d/17Z8PPhxIZWI7rZxW8bZHsq4HgIwFWmZyKfsCh_xHq8s/edit?gid=472240210"
spreadsheet = client.open_by_url(sheet_url)

# Access the "Training Set" sheet
sheet = spreadsheet.worksheet("Training Set")

# Get data from the range B2:Q17
data = sheet.get('B2:Q17')  # This will directly fetch the specific range

# Define the column headers manually
columns = [
    'Date', 'Favorite', 'Favorite Score', 'Underdog', 'Underdog Score', 'Spread',
    'Fav. At Home?', 'Winner', 'Favorite - Underdog (+/-)', 'Favorite Cover?', 'Favorite Win?',
    'Away', 'Away Score', 'Home', 'Home Score', 'Home/Away +/-'
]

# Convert data into a DataFrame and assign column names
df = pd.DataFrame(data, columns=columns)

# Save the data to a CSV file
df.to_csv("training_set_data.csv", index=False)
print("Data from the 'Training Set' sheet has been saved as training_set_data.csv")