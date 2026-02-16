import smtplib
import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()

# date_of_birth = dt.datetime(year=1999, month=11, day=25)

MY_EMAIL = "tum390730@gmail.com"
PASSWORD = "wibt ldhe rrxk xdrl"


if day_of_week == 0:
    with open("quotes.txt", mode="r") as data:
        data_quotes = data.readlines()
        random_quote = random.choice(data_quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="testando299@yahoo.com",
            msg=f"Subject:Monday Motivation!!\n\n{random_quote}."
        )
