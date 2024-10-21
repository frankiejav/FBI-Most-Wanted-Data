FBI Most Wanted Data Scraper

This Python script queries the FBI Wanted API and collects data about wanted individuals. The data is saved as a CSV file in a user-specified directory.

Features

1. Queries the FBI Wanted API to collect data on wanted individuals.

2. Automatically handles pagination to retrieve multiple pages of results.

3. Saves the data in a CSV format with a unique filename to avoid overwriting existing files.

Prerequisites

Before running the script, ensure you have the following installed:

Python 3.x
Required libraries:

    pip install requests pandas

Setup Instructions

Clone the Repository Clone the repository to your local machine:

    git clone https://github.com/YOUR-USERNAME/FBI-Most-Wanted-Data.git
    
    cd FBI-Most-Wanted-Data

Modify the save directory in the script, you'll need to specify the directory where the CSV files will be saved. Open fbi_wanted.py and locate this line:

    save_directory = '/path/to/your/download/directory'

Change '/path/to/your/download/directory' to the directory where you'd like the CSV files to be saved. For example:

    save_directory = '/home/frankie/Documents/FBIWANTED'

Run the Script after modifying the save directory, you can run the script:

    python fbi_wanted.py

File Handling:
The script will automatically create the directory if it does not exist. Additionally, if a file with the same name already exists, the script will append a number to the filename to prevent overwriting.

How it Works

    The script sends GET requests to the FBI Wanted API.
    It retrieves data in JSON format and normalizes it into a pandas DataFrame.
    The data is then saved in CSV format in the specified folder.
    The script handles pagination to retrieve multiple pages of results and sleeps between requests to avoid overwhelming the server.

Example

Here’s a quick example of what the data might look like in the saved CSV file:

Status, URL, Publication, Eyes, Race, ...

na, https://www.fbi.gov/wanted/cyber/mujtaba-raza, 2021-03-15T07:47:00, brown, ...

