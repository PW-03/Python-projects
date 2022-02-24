"""
Function that checks for prime numbers
"""
def isPrime(number):

    for num in range(1,number+1):
        count = True
        for i in range(2,num):
            if num % i == 0:
                count = False
        if count:
            print("{} is a prime number".format(num))
        else:
            print("{} is not a prime number".format(num))


if __name__ == "__main__":
    number = input("Please enter a whole number: ")
    isPrime(int(number))