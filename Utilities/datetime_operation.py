import datetime
import time


def datetime_menu():

    while True:  

        print("""
========================================
       Datetime and Time Operation
========================================

1. Display Current Date and Time
2. Calculate Difference Between Two Dates
3. Format Date into Custom Format
4. Stopwatch
5. Countdown Timer
6. Back To Main Menu
""")
      
      
        inner_user = int(input("Enter Your Choice Here...."))
      
        if inner_user == 1:
                  print(f"Current Date and Time : {datetime.datetime.now()}")
      
        elif inner_user == 2:
                  date1 = input("Enter first Your date (YYYY-MM-DD)")   
                  date2 = input("Enter Secound Your date (YYYY-MM-DD)") 
                  con_date1 =  datetime.datetime.strptime(date1,"%Y-%m-%d")  
                  con_date2 =  datetime.datetime.strptime(date2,"%Y-%m-%d")  
                  print(f"Diffenece: {(con_date1-con_date2).days} Days")
      
        elif inner_user ==3:
                  now =  datetime.datetime.now().date()
                  print(f"Current Date and Time : {now}")
                  user  = input("Enter Your Date format here like this format(%Y-%m-%d): ")
                  user_format = datetime.datetime.strftime(now , user)
                  print(f"Here is Your formated date: {user_format}")
      
        elif inner_user == 4:
                  start = input("Press Enter To start the Timer..")
                  if start == "":
                      start_time = datetime.datetime.now()
                  end = input("Press Enter To stop  the Timer..")
                  if end == "":
                      now = datetime.datetime.now()
                      end_time = now - start_time
                      print(f"Your Timing is {end_time.total_seconds()} Secound")
      
        elif inner_user == 5:
                  user = int(input("Enter a Secound to starts with: "))
                  while user > 0:
                      print(f" Tik Tik {user}")
                      time.sleep(1)
                      user-=1
                  print("Time's Up!")
      
        elif inner_user == 6:
                  print("Returning to the main menu...again")
                  break
      
        else:
                  print("Invaid input ")