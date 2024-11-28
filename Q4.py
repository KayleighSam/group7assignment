def maximum_number(): #Creating a function to find maximum value
    numbers = []
    for num in range(1, 6): # Allows users to enter 5 numbers
        while True:
            try:
                num = float(input(f"Enter number {num}: ")) #prompt users to enter a number for input
                numbers.append(num) # Puts the numbers into a single array
                break
            except ValueError:
                print("Invalid input.") #Error displayed if user does enter a number
    max_number = max(numbers)  # Find the maximum number
    print("You entered the following numbers:", numbers)
    print("The maximum number is:", max_number)


# Call the function
maximum_number()