# Directory Organizer
This is a Python script to automatically organize files in a folder into specific subfolders based on file type.

Usage

To use this script:

Clone this repository or download the file_organizer.py script
Install dependencies:

    pip install watchdog

Run the script:
```
python file_organizer.py
```
The script will organize them into subfolders.
Features

Automatically categorizes files based on extension into subfolders
Supports categorizing into Documents, Images, PDFs, Spreadsheets etc.
Ignores the file organizer script itself from moving
Provides console output when new files are organized
(later): Uses watchdog to monitor directory for changes
Organizes new files immediately after they are downloaded

Customization

To add new supported file types, modify the list in the script
Adjust the folder mapping logic to save files to customized locations

Requirements

Python 3.6+

watchdog module

License

This project is open source and available under the MIT License.
