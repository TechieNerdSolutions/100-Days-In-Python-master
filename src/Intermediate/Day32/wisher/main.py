from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "royalphoenixtnd@gmail.com"
MY_PASSWORD = "rvezgmuxbggtblil"
today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"src/Intermediate/Day32/wisher/quotes{random.randint(1,3)}.txt"
    with open(file_path) as quotes_file:
        contents = quotes_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["bkutalian@gmail.com"],
            msg=f"Subject:Happy Day!\n\n{contents}"
        )
