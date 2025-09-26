def length(N):
    count = 0
    num = N

    while num > 0:
        num //= 10
        count += 1
    
    return count

number = int(input("Enter a number you want to find how many digits are in it: "))

if number == 0:
    print("number of digits equal to 1")
else:
    print(length(number))