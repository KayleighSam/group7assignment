def main_menu():
    # List the menu options in the window
    while True:
        print("\nSIM1")
        print("1. Safaricom")
        print("2. Mpesa")
        # Allow user to input a choice
        choice = input("Enter Choice: ").strip()
        # Give conditions for the input choice made by the user
        if choice == "1":
            print("You have selected Safaricom")
        elif choice == "2":
            print("You have selected Mpesa")
            mpesaMenu()
            break
        elif choice.lower() == "exit":
            print("Exiting...")
            break
        else:
            print("Invalid Input. Try again.")

# Mpesa Function
def mpesaMenu():
    while True:
        print("\nM-PESA Menu")
        print("1. Send Money")
        print("2. Withdraw Money")
        print("3. Buy Airtime")
        print("4. Loans and Savings")
        print("5. Lipa na M-PESA")
        print("6. My Account")
        print("0. Back to Main Menu")
        choice = input("Enter Choice: ").strip()
        if choice == "1":
            print("You have selected Send Money")
            send_Money()
            return
        elif choice == "0":
            return
        else:
            print("Invalid Choice")

# Send Money Function    
def send_Money():
    while True:
        phoneNumber = input("Enter a Valid Phone Number (must be between 10-13 characters or 'back' to return): ")
        if phoneNumber.lower() == "back":
            return
        # Check condition using the validate phone number function
        elif validatePhone(phoneNumber):
            print(f"{phoneNumber} is a valid phone number.")
            break
        else:
            print(f"{phoneNumber} is an invalid phone number. Try again.")

# A function to validate phone numbers
def validatePhone(phoneNumber):
    if 10 <= len(phoneNumber) <= 13 and all(c.isdigit() or c in "*#+" for c in phoneNumber):
        return True
    return False

# Call the main menu function
main_menu()
