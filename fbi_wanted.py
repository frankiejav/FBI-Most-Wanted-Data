import requests
import pandas as pd
import os
import time

# Define the directory to save the CSV
save_directory = '/home/frankie/Documents/FBIWANTED'
os.makedirs(save_directory, exist_ok=True)  # Create directory if it doesn't exist

# Initialize an empty DataFrame
fbi_wanted_df = pd.DataFrame()

# Function to get data from the FBI Wanted API
def get_fbi_wanted(page):
    try:
        response = requests.get(f'https://api.fbi.gov/wanted/v1/list?page={page}')
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON data if the request was successful
    except requests.exceptions.HTTPError as err:
        print(f'HTTP error occurred: {err}')
        return None

# Function to generate a unique filename
def get_unique_filename(base_filename, directory):
    counter = 1
    filename = f"{base_filename}.csv"
    filepath = os.path.join(directory, filename)
    
    # If the file already exists, append a number to it
    while os.path.exists(filepath):
        filename = f"{base_filename}_{counter}.csv"
        filepath = os.path.join(directory, filename)
        counter += 1
    
    return filepath

# Retrieve data with pagination
page = 1
while True:
    content = get_fbi_wanted(page)
    if content is None or len(content['items']) == 0:
        break  # Exit loop if there's no content or if an error occurred

    # Append the items to the DataFrame
    fbi_wanted_df = pd.concat([fbi_wanted_df, pd.json_normalize(content['items'])], ignore_index=True)

    # Avoid getting blocked by the server
    time.sleep(1)  # Adjust the sleep time if needed

    page += 1

# Get a unique filename to prevent overwriting
output_file = get_unique_filename('fbi_wanted_data', save_directory)

# Save DataFrame to the unique CSV file
fbi_wanted_df.to_csv(output_file, index=False)
print(f'Data saved to {output_file}')
