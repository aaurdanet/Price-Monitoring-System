import requests
from bs4 import BeautifulSoup
import os
import smtplib

notification_receiver = os.environ.get("RECEIVER")
my_email = os.environ.get("SENDER_EMAIL")
my_password = os.environ.get("SENDER_PASSWORD")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Accept-Language": "en-US,en;q=0.5"
}


def smtp(product_price, product_name, receivers_email):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=f"{receivers_email}",
                        msg=f"Subject: Price Monitoring System\n\nHello!\n{product_name} is now ${product_price}")


amazon_response = requests.get(
    "https://www.amazon.com/Beats-Studio-Pro-Personalized-Compatibility/dp/B0C8PR4W22?ref_=Oct_DLandingS_D_35f80eae_2",
    headers=headers)
webpage = amazon_response.text

soup = BeautifulSoup(webpage, "lxml")

prince_find = soup.find(name="span", class_="a-offscreen")
price = prince_find.text
final_price = float(price.replace("$", ""))

product_title = soup.find(name="h1", id="title", class_="a-size-large a-spacing-none")
product = product_title.text.strip()

if final_price < 180:
    smtp(product_price=final_price, product_name=product, receivers_email=notification_receiver)
    print("Sent")

