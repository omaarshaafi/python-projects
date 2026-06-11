attempts = 0

while attempts < 5:
    number = int(input("Enter Your Password : "))

    if number == 7:
        print("You Have Been Authorized Successfully")
        break

    attempts += 1

    if attempts == 5:
        print("Reset Password")
    else:
        print("Retry Password")