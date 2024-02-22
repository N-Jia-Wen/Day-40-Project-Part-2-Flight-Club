# Run this code when registering a new user. This can also be a standalone file as it only communicates with Sheety API.
import requests

SHEETY_USER_ENDPOINT = "Input your Sheety API for the sheet containing your users' information here."

print("Welcome to FLight CLub!\nWe find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email? Please enter a Gmail, Hotmail, or Yahoo email address:\n")
confirm_email = input("Please type your email again to confirm.\n")
if email == confirm_email:
    new_user = {
        "user": {
            "firstName": first_name.title(),
            "lastName": last_name.title(),
            "email": email
        }
    }
    post_response = requests.post(url=SHEETY_USER_ENDPOINT, json=new_user)
    post_response.raise_for_status()
    if post_response.status_code == 200:
        print("You're in the club!")
    else:
        print("Sorry, an error occurred. Please try again later.")
else:
    print("Sorry, the emails do not match. Please enter your personal information again.")
