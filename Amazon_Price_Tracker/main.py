from bs4 import BeautifulSoup
from smtplib import SMTP
import requests

MY_EMAIL = "your_mail@gmail.com"
MY_PASSWORD = "your_password"

BUY_PRICE = 65000

url = 'https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1_sspa?crid=3NI6CHPNFP3EY&dib=eyJ2IjoiMSJ9.HvIbKicK-wBXX5On3-PhnSsXU75fq8Y4zSe_afkYWsKH5K7-H3vrsbxykxD7jFp2pTRds74qrxWugDi2m76jp8CuR48lA2XVismh5tL_w425sJi3BGz-Rgjhya6DHi2tTNOZRAVD-bgX9dRX8TDqjuZTza-X6B5KF0qShDPSV7m9YoBxrjGfFN-PFL0001YMnKOuKiaGgkLdWEcKue37-YkRotHewyig1Ff_92mDTMY.ceMPxD9nOhW7d1yUcY8BXzf8YlXnf_rtD8eDDzknwf8&dib_tag=se&keywords=macbook+air&qid=1719120150&sprefix=macbook+ai%2Caps%2C230&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'

headers = {
    "User-Agent":"Defined"
}

with requests.get(url=url, headers=headers) as response:
    response.raise_for_status()


soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("₹")[1]
price = float(price_without_currency.replace(",", ""))

title = soup.find(id="productTitle").get_text().strip()
print(title)


if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with SMTP("smtp.gmail.com", 587) as connection:

        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="other_mail@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
