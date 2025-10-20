from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import time
import random
import csv
import os

# -----------------------------
# CONFIGURATION
# -----------------------------
smtp_server = "smtp.gmail.com"
port = 465  # SSL port
sender_email = "projectw161@gmail.com"
password = "vctz huux elun htfn"  # App password only!

subject = " This is the Beginning of Greatness"
body = """\
    This is the beginning of good works
"""

# -----------------------------
# LOAD RECIPIENTS FROM FILE
# -----------------------------
def load_emails(file_path):
    emails = []

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    if file_path.endswith(".txt"):
        with open(file_path, "r") as f:
            emails = [line.strip() for line in f if line.strip()]
    elif file_path.endswith(".csv"):
        with open(file_path, "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and "@" in row[0]:
                    emails.append(row[0].strip())
    else:
        raise ValueError("⚠️ Unsupported file type. Please use .txt or .csv")

    if not emails:
        raise ValueError("⚠️ No emails found in the file!")

    return emails


# Path to your file — change this to your actual filename
email_file = "emails.txt"  # or "emails.csv"

recipients = load_emails(email_file)
print(f"📬 Loaded {len(recipients)} recipient emails from '{email_file}'")

# -----------------------------
# SAFETY & DELIVERY
# -----------------------------
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)

        # Create message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Use BCC to hide recipient list
        msg["To"] = sender_email
        msg["Bcc"] = ", ".join(recipients)

        # Send a single BCC email to all recipients
        server.sendmail(sender_email, recipients, msg.as_string())
        print(f"✅ Successfully sent email to {len(recipients)} recipients via BCC!")

        # Optional delay for safety
        time.sleep(random.uniform(1, 3))

except Exception as e:
    print("❌ Error sending email:", str(e))
