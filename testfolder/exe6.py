# Display numbers divisible by 5 from a list

def number_divisible_by5(numberList):
    for i in range(0, len(numberList)):
        if numberList[i] % 5 == 0:
            print(numberList[i])

numberList1 = [10, 23, 25, 77, 65, 90, 105]
number_divisible_by5(numberList1)

numberList1 = [16, 28, 25, 75, 65, 11, 101]
number_divisible_by5(numberList1)