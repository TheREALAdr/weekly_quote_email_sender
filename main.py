import smtplib
import random
import datetime as dt

gmail_testing_acc = "obviouslyafakeemailbroski@gmail.com"
gmail_app_password = "vqtlvqzpnjhufmto"
# gmail_smtp_connection = "smtp.gmail.com"

yahoo_testing_acc = "testing_468@yahoo.com"
# yahoo_smtp_connection = "smtp.mail.yahoo.com"

outlook_testing_acc = "testing_278@outlook.com"
# outlook_smtp_connection = "smtp.live.com"

time_now = dt.datetime.now()
current_weekday = time_now.weekday()

sunday_day_number = 6

print(dt.datetime.now())

if current_weekday == sunday_day_number:
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
    random_quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Starting TLS to encrypt and protect email content while sent
        connection.starttls()
        connection.login(user=gmail_testing_acc, password=gmail_app_password)
        connection.sendmail(from_addr=gmail_testing_acc,
                            to_addrs=yahoo_testing_acc,
                            msg=f"Subject:Quote for Sunday!\n\n{random_quote}"
                            )
print(current_weekday)
