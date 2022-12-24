Automated Email Sender (Python Version)

    This is a Python script that sends automated emails at a specified time.

Requirements
    Python 3
    The smtplib and datetime modules

Usage
    Modify the send_time variable in the script to specify the time when the email should be sent.
    Modify the to, subject, and body variables to specify the recipient's email address, the subject of the email, and the body of the email, respectively.
    Modify the server.login line to include your email address and password.
    Run the script using python email_sender.py.

---

Automated Email Sender (Google Spreadsheet Version)

    This is a script that can be run through google sheets to automatically send emails. Doesn't include the date and time function.

Requirements
    Google account
    Google spreadsheet
    Google spreadsheet scripts

Usage
    Format the google spreadsheet in 4 columns. 
    The first row should be labelled "Email", "Subject", "Person of Interest", and "Message".
    Under each of these headers should include the emails, subjects, POIs, and the intended message.
