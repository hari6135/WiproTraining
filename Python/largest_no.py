# largest of two numbers
num1 = int(input("Enter frst number: "))
num2 = int(input("Enter scnd number: "))

if num1 > num2:
    print("The largest number is: ",num1)
elif num2 > num1:
    print("The largest number is: ",num2)
else:
    print("Both are equal")

'''if num1 == num2:
    print("both the numbers are equal")
else:
    print("The largest number is =: ", max(num1,num2))
'''
# largest of three numbers
num1 = int(input("Enter frst number: "))
num2 = int(input("Enter scnd number: "))
num3 = int(input("Enter thrd number: "))

if num1 == num2 == num3:
    print("All the numbers are same")
else:
    print("The largest number is: ", max(num1,num2,num3))