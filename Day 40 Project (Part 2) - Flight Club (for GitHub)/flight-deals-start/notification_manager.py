from twilio.rest import Client
import smtplib

TWILIO_ACC_SID = "Enter your Twilio account SID here."
TWILIO_AUTH_TOKEN = "Enter your Twilio authentication token here."
TWILIO_PHONE_NO = "Enter your Twilio virtual phone number here."
VERIFIED_PHONE_NO = "Enter your personal phone number that is verified on Twilio here."
SENDER_EMAIL = "Enter your personal email address which you use to send flight deal notifications to your users here."
SENDER_PASSWORD = "Enter your email address' app password here."


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = TWILIO_ACC_SID
        self.auth_token = TWILIO_AUTH_TOKEN
        self.sender_phone_no = TWILIO_PHONE_NO
        self.receiver_phone_no = VERIFIED_PHONE_NO

    def send_message(self, price, dep_city, dep_airport, arrival_city, arrival_airport, outbound_date, inbound_date,
                     no_of_stopovers, stopover_city):
        if no_of_stopovers == 0:
            stopover_info = ""
        else:
            stopover_info = f"Flight has 1 stop over, via {stopover_city}."
        client = Client(self.account_sid, self.auth_token)

        client.messages \
            .create(
                body=f"Low price alert! Only S${price} to fly from "
                     f"{dep_city}-{dep_airport} to "
                     f"{arrival_city}-{arrival_airport}, from "
                     f"{outbound_date} to "
                     f"{inbound_date}.\n\n"
                     f"{stopover_info}",
                from_=self.sender_phone_no,
                to=self.receiver_phone_no
            )

    def send_email(self, price, dep_city, dep_airport, arrival_city, arrival_airport, outbound_date, inbound_date,
                     no_of_stopovers, stopover_city, users_data: list):
        if no_of_stopovers == 0:
            stopover_info = ""
        else:
            stopover_info = f"Flight has 1 stop over, via {stopover_city}."

        for club_member in users_data:
            recipient_email = club_member["email"]
            email_domain = recipient_email.split("@")[-1]
            first_name = club_member["firstName"]
            last_name = club_member["lastName"]

            # Considers whether user's email is a Gmail, Hotmail, or Yahoo email address:
            if email_domain == "gmail.com":
                connection = smtplib.SMTP("smtp.gmail.com")
            elif email_domain == "live.com" or email_domain == "hotmail.com":
                connection = smtplib.SMTP("smtp.live.com")
            elif email_domain == "yahoo.com":
                connection = smtplib.SMTP("smtp.mail.yahoo.com")
            else:
                print("Sorry, this email address is not supported.")
                return None

            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
            connection.sendmail(from_addr=SENDER_EMAIL,
                                to_addrs=recipient_email,
                                msg=f"Subject: Cheap Flight Alert!\n\n"
                                f"Dear {first_name} {last_name},\n\n"
                                f"Only S${price} to fly from "
                                f"{dep_city}-{dep_airport} to "
                                f"{arrival_city}-{arrival_airport}, from "
                                f"{outbound_date} to "
                                f"{inbound_date}.\n\n"
                                f"{stopover_info}"
                                )
            connection.close()
