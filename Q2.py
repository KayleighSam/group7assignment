#List array of numbers
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 10,11, 3, 4, 5]
#create a function to sort numbers
def is_sorted(numbers1):
    for num in range(len(numbers1)-1):
        if numbers1[num] > numbers1[num + 1]:
                return False

    return True
print(numbers1,"sorted numbers",is_sorted(numbers1))
print(numbers2,"not sorted",is_sorted(numbers2))