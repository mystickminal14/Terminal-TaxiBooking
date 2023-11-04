customerData = []
import Dashboard
def register():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name:")
   
    # Age Validation
    while True:
        try:
            age = int(input("Enter your age: "))
            if 14 <= age <= 99:
                break
            else:
                print("Only age between 14 and 99 can register.")
        except ValueError:
            print("Age must be a number.")
   
    # Phone Number Validation
    while True:
        phone = input("Enter your phone number: ")
        if len(phone) == 10 and phone.isdigit():
            break
        else:
            print("Please enter a valid phone number.")
   
    # Email Address Validation
    while True:
        email = input("Enter your email address: ")
        if "@" in email and "." in email :
            break
        else:
            print("Please enter a valid email address.")
    
    # Password Validation
    while True:
        password = input("Enter your desired password: ")
        if len(password) >= 9 :
            break
        else:
            print("Password must be greater than 8 characters")
    
    return firstName, lastName, age, phone, email, password

def register_users(firstName, lastName, age, phone, email, password):
    data = {
        'firstName': firstName,
        'lastName': lastName,
        'age': age,
        'phone': phone,
        'email': email,
        'password': password
    }
    customerData.append(data)

def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    for data in customerData:
        if data['email'] == email and data['password'] == password:
            print("Login Successful!")
            Dashboard.dashboard(data)
            return
        else:
              print("Login Failed. Email or password is incorrect.")
              login()

if __name__ == "__main__":
    print("Minal Taxi Booking System!")
    print("1. Click 1 to Login")
    print("2. Click 2 to register a new account")

    userInput = input("Enter your choice: ")
    
    if userInput == '1':
       
        login()
    
    elif userInput == '2':
        firstName, lastName, age, phone, email, password = register()
        if firstName == '' or lastName == '' or age == '' or phone == '' or email == '' or password == '':
            print('Please fill up the entire form')
        else:
            print("Registration successful!")
            register_users(firstName, lastName, age, phone, email, password)
            choice=input("Do you want to login? yes / no :")
            if choice=='YES' or choice=='yes':
                 login()

            else:
                print("Thanks for registration")
