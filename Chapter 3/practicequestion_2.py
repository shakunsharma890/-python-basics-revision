#question on slicing:-
#take input and print middle 3 character,last two character

str = input("enter the value:-")
mid = len(str)//2
output = str[mid-1:mid+2]
print(output)
output2 = str[-2:]
print(output2)