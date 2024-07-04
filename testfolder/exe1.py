#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the Second Number: "))

sum = number1 + number2
multification = number1 * number2

#print(type(product))

if multification >= 1000:
    print("Result is", sum)
else:
    print("Result is " , multification)

####################################################

# Solution using a function

def calculation(num1, num2):

    product = num1 * num2
    if product >= 1000:
        return num1 + num2
    else:
        return product
        
results = calculation(10,60)
print("The result is", results)

results = calculation(100,60)
print("The result is", results)
