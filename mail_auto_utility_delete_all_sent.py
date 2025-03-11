import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Zoho Mail Credentials
ZOHO_SMTP_SERVER = "smtp.zoho.com"
ZOHO_IMAP_SERVER = "imap.zoho.com"
EMAIL_ID = "vijay.nerkar@softzonik.com"
EMAIL_PASSWORD = "Mobile@Sgn$4"

# List of Recipients
recipients = ["VIJU.NERKAR4@GMAIL.COM", "vijurnerkar@gmail.com", "nts.nitin@gmail.com"]

# Email Content
subject = "Test Email"
body = "This is an automated email from Zoho Mail."

def send_email(to_email):
    try:
        server = smtplib.SMTP_SSL(ZOHO_SMTP_SERVER, 465)
        server.login(EMAIL_ID, EMAIL_PASSWORD)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ID
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(EMAIL_ID, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

def delete_sent_email():
    try:
        mail = imaplib.IMAP4_SSL(ZOHO_IMAP_SERVER)
        mail.login(EMAIL_ID, EMAIL_PASSWORD)
        mail.select('"Sent"')  # Folder for sent emails

        # Search for all emails in Sent folder
        result, data = mail.search(None, "ALL")
        email_ids = data[0].split()

        for e_id in email_ids:
            mail.store(e_id, "+FLAGS", "\\Deleted")

        mail.expunge()  # Permanently delete marked emails
        mail.logout()
        print("Sent emails deleted successfully")

    except Exception as e:
        print(f"Error deleting sent emails: {e}")

# Sending Emails
for recipient in recipients:
    send_email(recipient)

# Delete Sent Emails
delete_sent_email()
