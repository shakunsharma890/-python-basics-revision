# 💻 Section B: Coding Questions
''' 1️⃣ Smart Temperature Converter
Take input in Celsius and print its equivalent in Fahrenheit and Kelvin.
(Use explicit type conversion and arithmetic operators.)

Formula:
Fahrenheit = (C × 9/5) + 32
Kelvin = C + 273.15

Example:
Enter temperature in Celsius: 25
Output:
Fahrenheit: 77.0
Kelvin: 298.15
'''
celsius = int(input("enter you temperature in celsius:-"))
Fahrenheit = (celsius * (9/5)) + 32
kelvin = (celsius + 273.15)
print("Fahrenheit: ",Fahrenheit)
print("kelvin: ",kelvin)

'''
2️⃣ Bill Split Calculator
Write a program that takes total bill amount and number of friends as input.
Calculate how much each person will pay.
Also print the data type of each variable used.
(Hint: use float() and division operator)
Total bill: 1000
Friends: 4
Each will pay: 250.0
'''
total_bill = int(input('Tell me your total bill:-'))
friends = int(input('Tell me how many friends you all are:-'))
split_bill = total_bill/friends 
print("Each one of you will pay: ",split_bill)