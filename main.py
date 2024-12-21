import random
import smtplib
import datetime as dt

now =dt.datetime.now()
week_day = now.weekday()
my_emails = ["jaycool4050l@hotmail.com","blinzo4050@gmail.com","lin4050@hotmail.com"]

if week_day == 0:
    with open("quotes.txt") as data:
        new_list = data.readlines()

        my_email = "pmailer68@gmail.com"
        password = "mozfcdmqdnodkirz"
        for emails in my_emails:
            recipient_email = emails
            subject = "Greetings"
            body = random.choice(new_list)

            message = f"Subject: {subject}\n\n{body}"

            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(
                        from_addr=my_email,
                        to_addrs=recipient_email,
                        msg=message
                    )
                print("Email sent successfully!")
            except Exception as e:
                print(f"Error occurred: {e}")



