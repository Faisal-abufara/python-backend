import requests
import smtplib
from email.message import EmailMessage
import os
import info
def fetch_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={info.API_KEY}&q={city}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return {
            "location": data['location']['name'],
            "region": data['location']['region'],
            "country": data['location']['country'],
            "temp_c": data['current']['temp_c'],
            "condition": data['current']['condition']['text'],
            "humidity": data['current']['humidity'],
            "wind_kph": data['current']['wind_kph']
        }
    except Exception as e:
        print(f"Failed to fetch weather data: {e}")
        return None

def generate_report(data, filename):
    try:
        with open(filename, 'w') as f:
            f.write("Weather Report\n")
            f.write("====================\n")
            for key, value in data.items():
                f.write(f"{key.capitalize()}: {value}\n")
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Failed to write report: {e}")

def send_email_with_attachment(subject, body, to_email, from_email, password, attachment_path):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(body)

    try:
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(attachment_path)
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    except Exception as e:
        print(f"Failed to attach file: {e}")
        return

    try:
        with smtplib.SMTP(info.SMTP_SERVER, info.SMTP_PORT) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

weather_data = fetch_weather(info.CITY)
if weather_data:
    generate_report(weather_data, info.ATTACHMENT_FILE)
    email_body = f"Attached is the latest weather report for {info.CITY}."
    send_email_with_attachment(info.SUBJECT, email_body, info.RECEIVER_EMAIL, info.SENDER_EMAIL, info.PASSWORD, info.ATTACHMENT_FILE)
else:
    print("No data to send.")