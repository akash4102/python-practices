#  this is a program to capitalize all the first letter in the string 
# first we take input from the user
s=(str)(input())

# then we run a loop and split whole string by using .split() function
for x in s.split():
    #  then we simply use x.capitalize() function to capital letter in the string
    s=s.replace(x,x.capitalize())

# and finally we print the stirng and we got the result
print(s)