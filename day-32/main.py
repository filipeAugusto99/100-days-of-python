import smtplib


my_email = "tum390730@gmail.com"
password = "wibt ldhe rrxk xdrl"


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="testando299@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )
