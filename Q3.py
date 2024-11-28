#create variables for start number and end number
start_Number=10
end_Number=20
#create variables for skipping numbers that are divisible by 7
def numbers_skipping_seven(start_Number, end_Number):
    #for looping numbers in the range
    for num in range(start_Number,end_Number +1):
        if num % 7 == 0:
            continue
        print(num, end="")
        # print(f"Print numbers between {start_Number} and {end_Number}")
numbers_skipping_seven(start_Number, end_Number)