num = str(input("Enter a number you want to find how many digits are in it: "))
n = 0          

while n != len(num):
    n = n+1

print("number of digits in {0} is {1}.".format(num, n))