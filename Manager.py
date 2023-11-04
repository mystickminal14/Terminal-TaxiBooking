import Home
import Dashboard

def managerChoice(customerData, bookingDetails):
    choice = input("1/2/3")
    if choice == '1':
        print("Customers")
        for customer in customerData:
            print(f"Full Name: {customer['firstName']} {customer['lastName']} Age: {customer['age']} Email: {customer['email']} Phone Number: {customer['phone']} Password: {customer['password']}")
        user_CHOICE = input("Enter your choice (Y/N):")
        if user_CHOICE == 'Y' or user_CHOICE == 'y':
            managerDashboard(customerData, bookingDetails)
        else:
            managerDashboard(customerData, bookingDetails)
    elif choice == '2':
        print('Booking details')
        for booking in bookingDetails:
            print(f"Full Name: {customerData['firstName']} {customerData['lastName']} Email: {customerData['email']} Destination: {booking['place']} Time: {booking['time']} Day: {booking['day']}")
        user_CHOICE = input("Enter your choice (Y/N):")
        if user_CHOICE == 'Y' or user_CHOICE == 'y':
            managerDashboard(customerData, bookingDetails)
        else:
            managerDashboard(customerData, bookingDetails)
    elif choice == '3':
        Home.login()
    else:
        Home.login()

def managerDashboard(data):
    print(f"Welcome Mr. Minal")
    print("WELCOME TO TAXI BOOKING SYSTEM")
    print("You have the following options to choose from:\n1. View Customers\n2. View Booking\n3. Go back to login")
    choice = Dashboard.booking
    managerChoice(data, choice)
