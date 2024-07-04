# Check if the first and last number of a list is the same

def firstIsSameLast(numberList):    

    if numberList[0] == numberList[-1]:
        print("True")
    else:
        print("False")


numbers_x = [10, 20, 30, 40, 10]
firstIsSameLast(numbers_x)

numbers_y = [75, 65, 35, 75, 30]
firstIsSameLast(numbers_y)