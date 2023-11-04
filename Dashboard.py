import Home

def dashboard(detail):
    print(f"Welcome {detail['firstName']}")
    print("You have following option to do in your dashboard\n 1. Click one to display your profile 2. Click 2 to make bookings" )
    user_CHOICE=input("enter your choice")