import smtplib
import imaplib
import email
import os
import pandas as pd
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# 🟢 Paths for Local Files
BASE_PATH = "H:\\SoftZonik\\mail_auto_sent_utility\\data\input_file"
GENERATED_FILE_PATH = "H:\SoftZonik\mail_auto_sent_utility\data\Generate_File"
IMAGES_PATH = "H:\\SoftZonik\\mail_auto_sent_utility\\images"
EXCEL_FILE = os.path.join(BASE_PATH, "email_data.xlsx")
NEW_EXCEL_FILE = os.path.join(GENERATED_FILE_PATH, "email_data_with_sent_date.xlsx")  # Output file
IMAGE_FILE = os.path.join(IMAGES_PATH, "initial.jpg")  # Banner Image

# Social Media Icons (Local Files)
SOCIAL_MEDIA_ICONS = {
    "youtube": os.path.join(IMAGES_PATH, "youtube.PNG"),
    "whatsapp": os.path.join(IMAGES_PATH, "whatsup.PNG"),
    "facebook": os.path.join(IMAGES_PATH, "facebook.PNG"),
    "linkedin": os.path.join(IMAGES_PATH, "linkedLin.PNG"),
    "instagram": os.path.join(IMAGES_PATH, "instagram.PNG"),
}

# Clickable Social Media Links
SOCIAL_MEDIA_LINKS = {
    "youtube": "https://www.youtube.com/@softzonik2417",
    "whatsapp": "https://wa.link/14stn3",
    "facebook": "https://www.facebook.com/SZonikAcademy/",
    "linkedin": "https://www.linkedin.com/company/softzonik/",
    "instagram": "https://www.instagram.com/softzonik_academy/",
}

# 🟢 Zoho Mail Credentials
ZOHO_SMTP_SERVER = "smtp.zoho.com"
ZOHO_IMAP_SERVER = "imap.zoho.com"
EMAIL_ID = "vijay.nerkar@softzonik.com"
EMAIL_PASSWORD = "Mobile@Sgn$4"  # Use an App Password if needed

DATE_COLUMN = "Mail Sent Date"  # Column to store the sent date

def read_email_list():
    """Reads only the required columns from the input Excel file."""
    try:
        df = pd.read_excel(EXCEL_FILE, usecols=["company_name", "First Name", "mail id"])

        # Add Mail Sent Date column if it does not exist
        if DATE_COLUMN not in df.columns:
            df[DATE_COLUMN] = ""

        print(f"✅ Loaded {len(df)} contacts from Excel.")
        return df
    except Exception as e:
        print(f"❌ Error reading Excel file: {e}")
        return pd.DataFrame()

def attach_image(msg, image_path, cid):
    """ Attaches an image and sets a Content-ID (cid) for embedding in HTML. """
    with open(image_path, "rb") as img:
        mime_img = MIMEImage(img.read())
        mime_img.add_header("Content-ID", f"<{cid}>")
        mime_img.add_header("Content-Disposition", "inline", filename=cid)
        msg.attach(mime_img)

def send_email(company, name, to_email):
    """Sends an email, logs sent date, and deletes sent email from Zoho. """
    try:
        server = smtplib.SMTP_SSL(ZOHO_SMTP_SERVER, 465)
        server.login(EMAIL_ID, EMAIL_PASSWORD)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_ID
        msg["To"] = to_email
        msg["Subject"] = "Business Collaboration Opportunity"

        # Attach images
        attach_image(msg, IMAGE_FILE, "logo")
        for key, image_path in SOCIAL_MEDIA_ICONS.items():
            attach_image(msg, image_path, key)

        # HTML Email Template with Proper Formatting
         # HTML Email Template with Smaller Social Media Icons
        html_content = f"""
        <html>
        <body style="background-color:#121212; color:white; font-family:Arial, sans-serif;">
            <img src="cid:logo" alt="Business Strategy" style="width:100%; max-height:200px; object-fit:cover;">
            <h2>Transform Your Business with Cutting-Edge Software Solutions</h2>
            <p>Dear <b>{name}</b>,</p>
            <p>In today’s digital world, <b>customized software can be the game-changer for your business.</b> 
            At <b>SoftZonik</b>, we specialize in delivering <b>high-quality, scalable, and innovative software solutions</b> tailored to your needs.</p>

            <h3>💡 Our Expertise:</h3>
            <ul>
                <li>✔ <b>Web & Mobile App Development</b> – User-Friendly, Scalable & Secure Solutions</li>
                <li>✔ <b>Custom Websites</b> – Static and dynamic websites</li>
                <li>✔ <b>Software Development</b> – Custom, AI, Automation & Smart Integrations</li>
                <li>✔ <b>IT Consulting</b> – Your problem is now OUR problem</li>
                <li>✔ <b>Cloud Hosting</b> – Efficient & Cost-Saving Hosting</li>
                <li>✔ <b>Corporate Training</b> – Customized training per your need</li>
            </ul>

            <p>🚀 <b>Let’s Build Something Amazing Together!</b></p>
            <p>📞 <b>Schedule a Free Consultation</b> to discuss how we can transform your business!</p>

            <p><a href="mailto:vijay.nerkar@softzonik.com" style="color:#ffcc00;">📩 Let’s Talk | 📧 Reply to This Email</a></p>

            <p>🔥 <b>Limited Projects Onboarded Monthly – Secure Your Spot Now!</b></p>

            <p>Best Regards,</p>
            <p><b>Nitin Shinde</b><br>
            Founder, SoftZonik<br>
            📞 +91-976-495-9860<br>
            🌍 <a href="https://www.softzonik.com" style="color:#ffcc00;">www.softzonik.com</a>
            </p>

            <!-- Social Media Links with Smaller Icons -->
            <p>
                <a href="{SOCIAL_MEDIA_LINKS['youtube']}" target="_blank">
                    <img src="cid:youtube" width="25" height="25">
                </a>
                <a href="{SOCIAL_MEDIA_LINKS['whatsapp']}" target="_blank">
                    <img src="cid:whatsapp" width="25" height="25">
                </a>
                <a href="{SOCIAL_MEDIA_LINKS['facebook']}" target="_blank">
                    <img src="cid:facebook" width="25" height="25">
                </a>
                <a href="{SOCIAL_MEDIA_LINKS['linkedin']}" target="_blank">
                    <img src="cid:linkedin" width="25" height="25">
                </a>
                <a href="{SOCIAL_MEDIA_LINKS['instagram']}" target="_blank">
                    <img src="cid:instagram" width="25" height="25">
                </a>
            </p>

        </body>
        </html>
        """



        msg.attach(MIMEText(html_content, "html"))
        server.sendmail(EMAIL_ID, to_email, msg.as_string())
        server.quit()

        print(f"✅ Sent email to {to_email} (Hi {name})")

        # Delete the email from Sent Items
        delete_sent_email(msg["Subject"])

        return datetime.now().strftime("%d-%m-%y")  # Return the sent date

    except Exception as e:
        print(f"❌ Failed to send email to {to_email}: {e}")
        return ""

def delete_sent_email(to_email):
    """Deletes the sent email from Zoho's Sent Items based on recipient email."""
    try:
        mail = imaplib.IMAP4_SSL(ZOHO_IMAP_SERVER)
        mail.login(EMAIL_ID, EMAIL_PASSWORD)

        # ✅ Identify the correct Sent folder
        status, folders = mail.list()
        sent_folder = None
        for folder in folders:
            folder_name = folder.decode().split(' "/" ')[-1].strip('"')
            if "Sent" in folder_name:
                sent_folder = folder_name
                break
        
        if not sent_folder:
            print("⚠️ Sent folder not found. Email deletion skipped.")
            return

        mail.select(sent_folder)  # Open Sent Items folder

        # ✅ Search for emails sent TO the recipient
        result, data = mail.search(None, f'TO "{to_email}"')

        if result == "OK" and data[0]:
            email_ids = data[0].split()
            for email_id in email_ids:
                mail.store(email_id, "+FLAGS", "\\Deleted")  # Mark email for deletion
            mail.expunge()  # ✅ Permanently delete marked emails
            print(f"🗑️ Deleted sent email to: {to_email}")
        else:
            print(f"⚠️ No matching sent email found for: {to_email}")

        mail.logout()

    except Exception as e:
        print(f"❌ Failed to delete sent email: {e}")


# 🚀 **Main Execution**
if __name__ == "__main__":
    df = read_email_list()
    if not df.empty:
        for index, row in df.iterrows():
            sent_date = send_email(row["company_name"], row["First Name"], row["mail id"])
            df.at[index, DATE_COLUMN] = sent_date  # Update sent date column

        # Save updated data to a new Excel file
        df.to_excel(NEW_EXCEL_FILE, index=False)
        print(f"✅ Updated Excel file saved as: {NEW_EXCEL_FILE}")
