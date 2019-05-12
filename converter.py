user_name = input("Please enter your name: ")
print("Hello " + user_name + ", this program converts values in km to nautical miles")

while True:
    distance = float(input("Enter distance in km: "))

    print("Nautical miles", distance/1.8)

    again = input("Would you like to convert again(yes/no)? ")
    if again == "no":
        print("Thank you for using our service")
        break
    elif again == "yes":
        print("We are happy to oblige")





