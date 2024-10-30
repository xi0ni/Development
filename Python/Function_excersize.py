"""Exercise 82: Taxi Fare

In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters traveled. Write a function that takes the distance traveled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function."""

distance = int(input("how many kilometers did you travel? "))


def fare(x):
    base = 4
    meters = 0.25 / 140
    distance = x * 1000
    total_fare = base + (meters * distance)
    return total_fare


total_fare = fare(distance)
print(f"the total fare of the taxi ride is ${total_fare:.2f}")


"""
Exercise 88: Is it a Valid Triangle?
(33 Lines)
If you have 3 straws, possibly of differing lengths, it may or may not be possible
to lay them down so that they form a triangle when their ends are touching. For
example, if all of the straws have a length of 6 inches. then one can easily construct
an equilateral triangle using them. However, if one straw is 6 inches. long, while the
other two are each only 2 inches. long, then a triangle cannot be formed. In general,
if any one length is greater than or equal to the sum of the other two then the lengths
cannot be used to form a triangle. Otherwise they can form a triangle.
Write a function that determines whether or not three lengths can form a triangle.
The function will take 3 parameters and return a Boolean result. In addition, write a
program that reads 3 lengths from the user and demonstrates the behaviour of this
function."""


a = input("tell me the length of the first straw: ")
b = input("tell me the length of the second straw: ")
c = input("tell me the length of the third straw: ")


def triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


if triangle(a, b, c):
    print("this is a triangle")
else:
    print("this is not a triangle")


"""A prime number is an integer greater than 1 that is only divisible by one and itself.
Write a function that determines whether or not its parameter is prime, returning True 
if it is, and False otherwise. Write a main program that reads an integer from the user.   
and displays a message indicating whether or not it is prime. Ensure that the main program
will not run if the file containing your solution is imported into another program"""


number_input = int(input("input a number "))


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


if is_prime(number_input):
    print(f"{number_input} is a prime number")
else:
    print(f"{number_input} is not a prime number")

"""
In this exercise you will write a function that determines whether
or not a password is good. We will define a good password to be a 
one that is at least 8 characters long and contains at least one 
uppercase letter, at least one lowercase letter, and at least one number.
Your function should return true if the password passed to it as its
only parameter is good. Otherwise it should return false. Include a 
main program that reads a password from the user and reports whether or not it is
"""

password = input("Enter a password: ")


def is_good_password(password):
    # Check if the password meets all criteria
    if (
        len(password) > 8
        and any(char.isupper() for char in password)
        and any(char.islower() for char in password)
        and any(char.isdigit() for char in password)
    ):
        return True
    else:
        return False


if is_good_password(password):
    print("The password is good")
else:
    print("The password is bad")
