# Write your code below this line ๐


def prime_checker(number):
    notPrime = False
    for d in range(2, number - 1):
        if number % d == 0:
            notPrime = True
            break
    if notPrime:
        print("It's not a prime number.")
    elif not notPrime:
        print("It's a prime number.")


# Write your code above this line ๐

# Do NOT change any of the code below๐
n = int(input("Check this number: "))

prime_checker(number=n)
