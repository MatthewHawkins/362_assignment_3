chosen_year = int(input("Hello! Please enter a number to determine if it is a leap year: "))

if chosen_year % 4 != 0:
    print("Your year is not a leap year!")
else:
    if chosen_year % 100 == 0:
        if chosen_year % 400 == 0:
            print("Your year is a leap year!")
        else:
            print("Your year is not a leap year!")
    else:
        print("Your year is a leap year!")