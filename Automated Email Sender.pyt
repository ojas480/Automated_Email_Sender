import smtplib
import datetime

send_time = datetime.time(hour=12, minute=0, second=0)

while True:
    current_time = datetime.datetime.now().time()

    if current_time >= send_time:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        server.login("user_email@example.com", "user_email_pass")

        to = "recipient@example.com"
        subject = "Subject of Email"
        body = "This is an automated email sent from Python"
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("your_email_address@example.com", to, msg)

        server.quit()
        break