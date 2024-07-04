# Print the sum of the current number and the previous number
previous_num = 0

range_value = input("Enter the value that you want to see the sum of the current number and the previous number: ")
range_value = int(range_value) + 1
print(type(range_value))

for i in range(1,range_value):
    sum = previous_num + i
    print("Previous number is: ", previous_num, "Current number is: ", i, "The sum is", sum )

    previous_num = i