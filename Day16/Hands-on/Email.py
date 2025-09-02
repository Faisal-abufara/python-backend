import smtplib
import os
from email.message import EmailMessage
import socket

Sender_Email = input("Sender Email: ")
Password = input("Password: ")
Receiver_Email = input("Receiver Email: ")
Subject = input("Subject: ")
Message = input("Message: ")
Attachment_Path = input("Path to attachment (leave empty if none): ")


smtp_server = "smtp.gmail.com"
port = 587

def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=5):
            return True
    except Exception as e:
        print(f"Cannot connect to {host} on port {port}: {e}")
        return False

if not check_port(smtp_server, port):
    print("Exiting due to connection problem.")
    exit()

msg = EmailMessage()
msg['From'] = Sender_Email
msg['To'] = Receiver_Email
msg['Subject'] = Subject
msg.set_content(Message)

if Attachment_Path:
    if os.path.isfile(Attachment_Path):
        with open(Attachment_Path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(Attachment_Path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    else:
        print("Attachment path is invalid, skipping attachment.")

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(Sender_Email, Password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")