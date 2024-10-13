# get the three numbers from user
num1 = int(input("Enter number one "))
num2 = int(input("Enter number two "))
num3 = int(input("Enter number three "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print(f'The largest number is {largest}')
print(f'The smallest number is {smallest}')