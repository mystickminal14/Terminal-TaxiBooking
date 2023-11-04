import Home
import random
booking=[]
def bookingValidation():
      place=input("Which place do you want to travel to :")
      while True:
            time=input("Enter pickup time ! use (.. : .. AM/PM) FORMAT :")
            chose= 'AM' or 'PM'
            try:
                if ':'in time and chose in time:
                    break
                else : 
                    print("enter correct time")
            except Exception:
                print(Exception)
      day=input("Enter pick up day (sun/mon/tue/wed/thurs/fri/sat) :")
      book={
           'place':place,
           'time':time,
           'day':day,
          
      }
      booking.append(book)
      return place,time ,day
      
def view():
     if  not  booking:
          print('There are no records to display !')
     else:
          print(f"Travel Destination :{booking['place']}\n Time :{booking['time']} day :{booking['day']}")
     sure=input("Do you want to cancel or go to dashboard. Type 1 for booking and 2 for dashboard :")
     if sure =='1':
       if not booking:
            print("there are no data to be canceled")
       else:
             booking.clear()
             print('your booking successfully canceled')
     else:
        detail=Home.customerData
        dashboard(detail)

def payment(place,time,day):
     random_number = random.randint(200, 1000)
    
     print(f"Travel Destination :{place}\n Time :{time} day :{day}")
     print(f"Your total cost :{random_number}")
     sure=input("Are u sure you want to book (Y/N)")
     if sure=='y' or sure=='Y':
          print("Congratulation you have successfully requested your booking")
          sure=input("Do you want to view booking or go to dashboard. Type 1 for booking and 2 for dashboard :")
          if sure =='1':
               view(place,time,day)
          else:
                detail=Home.customerData
                dashboard(detail)

     else:
       detail=Home.customerData
       dashboard(detail)
  
def makeBooking():
    print("welcome to booking")
    place,time,day=bookingValidation()
    anotherChoice=input("You have to options. \n 1. Type 1 to to make payment \n 2. Type 2 to pay on rides and got to dashboard :")
    if anotherChoice=='2':
       detail=Home.customerData
       dashboard(detail)
    elif anotherChoice=='1':
         payment(place,time,day)
         
   

def customerChoice(customerData):
        print("You have following option to do in your dashboard\n 1. Click one to display your profile 2. Click 2 to make bookings 3. Click 3 to view booking 4. Click 4 to go back to login" )
        user_CHOICE=input("enter your choice :")
        if user_CHOICE=='1':
            print(f"Welcome  {customerData['firstName']} to your profile")
            print(f"Full Name :{customerData['firstName']} {customerData['lastName']}")
            print(f"Age :{customerData['age']}\n Email :{customerData['email']}\n Phone Number :{customerData['phone']}\n Password :{customerData['password']}")
            goto=input("Do you want to go to Dashboard:(Y/N) :")
            if goto=='y' or goto=='Y':
                    customerChoice(customerData)
            else:
                    user_CHOICE=='1'

        elif user_CHOICE=='2':
            makeBooking()

            goto=input("Do you want to go to Dashboard:(Y/N) :")
            if goto=='y' or goto=='Y':
                    customerChoice(customerData)
            else:
                    user_CHOICE=='1'

        elif user_CHOICE=='3' :
           view()
        elif user_CHOICE=='4' :
            Home.login()
        else:
            Home.login()
             

       
    
def dashboard(detail):
    print(f"Welcome {detail['firstName']}")
    customerChoice(detail)



        
       
         
        
  