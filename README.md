### ✅ **README for `MailAutoSendLogger`**  

Here’s a **professional README** for your GitHub repository:

---

# 📧 **MailAutoSendLogger**  
**Automated Email Sending Utility with Logging & Tracking**  

🚀 `MailAutoSendLogger` is a Python-based email automation utility that:  
✔ **Sends personalized HTML emails** using Zoho SMTP.  
✔ **Embeds images (banners & social media icons)** directly in the email.  
✔ **Reads recipient data from an Excel file (`email_data.xlsx`)**.  
✔ **Logs the email sent date (`DD-MM-YY`)** in a new file (`email_data_with_sent_date.xlsx`).  
✔ **Ensures security** by using environment variables for email credentials.  

---

## 📌 **Features**  
✅ **Bulk Email Sending** – Send emails to multiple recipients from an Excel sheet.  
✅ **Personalized Emails** – Uses recipient's name in the greeting.  
✅ **Embedded Images** – Adds a banner and clickable social media icons.  
✅ **Email Tracking** – Logs when each email is sent.  
✅ **Security** – Uses environment variables to store email credentials.  
✅ **Git Ignore Support** – Excludes sensitive files from commits.  

---

## 🛠 **Installation & Setup**  

### 🔹 **1. Install Dependencies**  
Ensure you have Python installed, then run:  
```bash
pip install pandas openpyxl smtplib email
```

### 🔹 **2. Set Up Environment Variables (Security)**  
To avoid hardcoding passwords, set your Zoho email password as an environment variable:  

For **Windows (Command Prompt):**  
```cmd
setx ZOHO_PASSWORD "your-email-password"
```

For **Linux/macOS (Terminal):**  
```bash
export ZOHO_PASSWORD="your-email-password"
```

---

## 📂 **Folder Structure**  
```
📁 MailAutoSendLogger
 ┣ 📂 data
 ┃ ┣ 📄 email_data.xlsx               # Input Excel file with email recipients
 ┃ ┣ 📄 email_data_with_sent_date.xlsx # Output file with sent timestamps
 ┃ ┣ 🖼️ initial.jpg                    # Email banner image
 ┃ ┣ 🖼️ youtube.PNG                     # Social media icons
 ┃ ┣ 🖼️ facebook.PNG                    # "
 ┃ ┣ 🖼️ linkedIn.PNG                    # "
 ┃ ┣ 🖼️ instagram.PNG                   # "
 ┃ ┣ 🖼️ whatsapp.PNG                     # "
 ┣ 📜 email_script.py                    # Main Python script
 ┣ 📜 .gitignore                         # Git ignore file
 ┣ 📜 README.md                           # This file
```

---

## 📊 **How to Use**
### 🔹 **1. Prepare the Excel File** (`email_data.xlsx`)  
| First Name | mail id                    |
|------------|----------------------------|
| Vijay      | vijay.nerkar@gmail.com     |
| Nitin      | nitin.shinde@example.com   |
| Simran     | simran.kapoor@example.com  |

---

### 🔹 **2. Run the Script**  
```bash
python email_script.py
```
🔹 The script will:  
✔ Read the **email list** from `email_data.xlsx`.  
✔ Send **personalized HTML emails** to each recipient.  
✔ Log the **sent date** in a new Excel file (`email_data_with_sent_date.xlsx`).  

---

## 🔗 **Social Media Links in Emails**  
📌 **Each email includes clickable icons for:**  
- 🌍 **[Website](https://www.softzonik.com)**  
- 📘 **[Facebook](https://www.facebook.com/SZonikAcademy/)**  
- 📷 **[Instagram](https://www.instagram.com/softzonik_academy/)**  
- 💼 **[LinkedIn](https://www.linkedin.com/company/softzonik/)**  
- 🎥 **[YouTube](https://www.youtube.com/@softzonik2417)**  
- 📲 **[WhatsApp](https://wa.link/14stn3)**  

---

## ❌ **.gitignore (Recommended)**
To prevent committing unnecessary files, create a `.gitignore` file with:  
```gitignore
# Ignore system files
.DS_Store
Thumbs.db

# Ignore Python cache
__pycache__/
*.pyc

# Ignore logs and temp files
*.log
*.tmp

# Ignore virtual environments
venv/
env/

# Ignore Excel files (optional, if you don’t want them in Git)
*.xlsx

# Ignore VS Code settings (optional)
.vscode/
```

---

## 💡 **Contributing**
We welcome contributions! To contribute:  
1. **Fork the repo**  
2. **Create a new branch** (`feature-name`)  
3. **Commit your changes**  
4. **Submit a pull request**  

---

## 📄 **License**
This project is **open-source** under the [MIT License](LICENSE).  

---

### 🎯 **Now Your Git Repo is Ready with a Complete README!**
Let me know if you need any modifications! 🚀😊
