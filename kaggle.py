import zipfile
import os

# Path to the ZIP file
zip_file_path = '/workspaces/SQL-Project/sports-data.zip'

# Directory to extract to
extracted_dir = '/workspaces/SQL-Project/extracted_data/'

# Extract ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

print("Files extracted to:", extracted_dir)

####

import pandas as pd

# Path to the extracted Excel file
extracted_excel_file = '/workspaces/SQL-Project/extracted_data/MLB'

# Load the specific sheets you want (MLB Statistics and MLB Salaries)
sheets_to_load = ['MLB Statistics', 'MLB Salaries']
dfs = pd.read_excel(extracted_excel_file, sheet_name=sheets_to_load)

# Save the dataframes to separate CSV files
dfs['MLB Statistics'].to_csv('MLB_Statistics.csv', index=False)
dfs['MLB Salaries'].to_csv('MLB_Salaries.csv', index=False)

print("Sheets 'MLB Statistics' and 'MLB Salaries' have been saved as CSV.")
