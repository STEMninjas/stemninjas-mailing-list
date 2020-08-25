# STEMninjas Mailing List

The mailing list is utilized for mass email applications (parent list, volunteer announcement, newsletter, etc.) and uses Google Drive/Sheets API to webscrape email addresses from Google Spreadsheets.
## Installation

After [downloading](https://github.com/STEMninjas/mailing-list/archive/master.zip) the repository, make sure the file structure is intact.

```bash
src
├── data
|   ├── client_data.json
│   ├── email_data_loc.txt
│   └── email_message_text.txt
└── mailr.py
```

## Usage
### mailr.py
Official naming of the application is **Mailr**. Make sure to fill all user-specific information:
```python
# ...
sheet_name="SPREADSHEET_NAME_HERE"
# ...
email_user = 'SENDER_EMAIL_HERE'
email_password = 'SENDER_PASSWORD_HERE'
subject = 'EMAIL_SUBJECT_HERE'
# ...
```
When choosing a range, if you want only 1 email in a specific cell, please type the cell number for both the first and last values of range. 
### client_data.json
Required to access spreadsheets. All Google Spreadsheets must be shared with the following email in order for the API to be utilized:
```json
"client_email": 
"testingemails@testingemails-286918.iam.gserviceaccount.com"
```
### email_data_loc.txt
Contains the location of `client_data.json` so that user does not need to re-enter file location continuously (in case file must be moved). 

### email_message_text.txt
User can write the message they want to send in `email_message_text.txt`. All links must contain "https://" in order to hyperlink. *Test email example*:
``` bash
Hello there,

This is random email. Please visit my link, https://www.python.org.

Thanks,
John Doe
```

## Questions
Please email contactstemninjas@gmail.com with any questions/concerns.
