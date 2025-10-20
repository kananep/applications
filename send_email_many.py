from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import ssl
import time
import random

# -----------------------------
# GMAIL SMTP CONFIGURATION
# -----------------------------
smtp_server = "smtp.gmail.com"
port = 465  # SSL port
sender_email = "projectw161@gmail.com"
password = "vctz huux elun htfn"  # <-- This must be an App Password, not your Gmail login

# -----------------------------
# RECIPIENT LIST
# -----------------------------
# You can replace this with a list loaded from a file (CSV, TXT, etc.)
recipients = [
    "projectw161@gmail.com",
    "kofiananepoku@gmail.com",
    "dianahagan@gmail.com",
    # Add up to 100 recipients here
]

# -----------------------------
# EMAIL DETAILS
# -----------------------------
subject = "Marketing"
body = """\
Hello,

This is a test email sent automatically using a secure Gmail SMTP connection.

Best regards,
Your Python Script
"""

# -----------------------------
# SAFETY + DELIVERY NOTES
# -----------------------------
# ⚠️ Gmail limits ~500 emails/day for regular accounts.
# ⚠️ Sending too many too fast may trigger temporary blocks or 'suspicious activity'.
# ✅ To stay safe, we include random small delays between sends.
# ✅ Use BCC (Blind Carbon Copy) to hide recipient list from others.
# ✅ Always use your App Password, never your real Gmail password.

# Create secure SSL context
context = ssl.create_default_context()

try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)

        # Create the base message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Add all recipients to BCC to hide emails from each other
        msg["To"] = sender_email  # for record
        msg["Bcc"] = ", ".join(recipients)

        # Send a single email with all recipients in BCC
        server.sendmail(sender_email, recipients, msg.as_string())
        print(f"✅ Bulk email sent successfully to {len(recipients)} recipients via BCC!")

        # Delay (just one email, but safe pattern)
        time.sleep(random.uniform(1, 3))

except Exception as e:
    print("❌ Error sending email:", str(e))
