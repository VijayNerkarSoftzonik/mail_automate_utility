import smtplib
import imaplib
import email
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid

# Zoho Mail Credentials
ZOHO_SMTP_SERVER = "smtp.zoho.com"
ZOHO_IMAP_SERVER = "imap.zoho.com"
EMAIL_ID = "vijay.nerkar@softzonik.com"
EMAIL_PASSWORD = "Mobile@Sgn$4"

# List of Recipients
recipients = ["VIJU.NERKAR4@GMAIL.COM", "vijurnerkar@gmail.com", "nds.nitin@gmail.com"]


# Email Content
subject = "Test Email"
body = "This is an automated email from Zoho Mail."

# Store the Message-IDs of sent emails
sent_message_ids = []

def send_email(to_email):
    try:
        server = smtplib.SMTP_SSL(ZOHO_SMTP_SERVER, 465)
        server.login(EMAIL_ID, EMAIL_PASSWORD)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ID
        msg["To"] = to_email
        msg["Subject"] = subject
        
        # Generate a unique Message-ID
        message_id = f"<{uuid.uuid4()}@zoho.com>"
        msg["Message-ID"] = message_id
        msg.attach(MIMEText(body, "plain"))

        # Send Email
        server.sendmail(EMAIL_ID, to_email, msg.as_string())
        server.quit()

        print(f"✅ Email sent to {to_email} with Message-ID: {message_id}")
        sent_message_ids.append(message_id)  # Store sent email's Message-ID

    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")

def delete_sent_email():
    try:
        mail = imaplib.IMAP4_SSL(ZOHO_IMAP_SERVER)
        mail.login(EMAIL_ID, EMAIL_PASSWORD)

        # Select the "Sent" mailbox
        status, messages = mail.select("Sent")  # Try "Sent", "Sent Items", or "Sent Messages"

        if status != "OK":
            print("Error selecting Sent folder:", status)
            return

        for message_id in sent_message_ids:
            search_criteria = f'HEADER Message-ID {message_id}'
            result, data = mail.search(None, search_criteria)

            if result == "OK":
                email_ids = data[0].split()
                if email_ids:
                    for e_id in email_ids:
                        mail.store(e_id, "+FLAGS", "\\Deleted")  # Mark email as deleted
                    mail.expunge()  # Permanently delete
                    print(f"✅ Deleted email with Message-ID: {message_id}")
                else:
                    print(f"❌ Email with Message-ID {message_id} not found.")
            else:
                print(f"❌ Error searching for Message-ID {message_id}.")

        mail.logout()

    except Exception as e:
        print(f"❌ Error deleting sent emails: {e}")

# Send Emails and Delete Just Those Emails
for recipient in recipients:
    send_email(recipient)

# Wait a few seconds to allow the email to be saved in "Sent" folder
time.sleep(5)

# Delete Only the Sent Emails
delete_sent_email()
