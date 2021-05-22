




def leap_year(chosen_year):
    # while True:
    #     chosen_year = int(input("Hello! Please enter a positive number to determine if it is a leap year: "))
    #     if chosen_year >= 0:
    #         break

    if chosen_year % 4 != 0:
        print("Your year is not a leap year!")
        return False
    else:
        if chosen_year % 100 == 0:
            if chosen_year % 400 == 0:
                print("Your year is a leap year!")
                return True
            else:
                print("Your year is not a leap year!")
                return False
        else:
            print("Your year is a leap year!")
            return True