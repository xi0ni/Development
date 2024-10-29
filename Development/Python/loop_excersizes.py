# 1) #coin flip simulation ##############################################################
import random

import random

average = 0


def coin_flip():
    head = 0
    tails = 0
    count = 0

    while True:
        flip = random.randint(0, 1)
        if flip == 0:
            print("H")
            head += 1
            tails = 0
        else:
            print("T")
            tails += 1
            head = 0
        count += 1

        if head == 3 or tails == 3:
            break
    return count


total_average = 0
for x in range(10):
    result = coin_flip()
    average += result
    print(f"  it took {result} flips to get 3 in a row")

average = average / 10
print(
    f"The average coin flips it took to get 3 heads or tails in a row in 10 games was {average:.2f} times"
)

# 2) MAXUMUM INTERGER ########################################################


import random

max_value = random.randint(1, 100)
update_count = 0

for x in range(99):
    new_integer = random.randint(1, 100)
    if new_integer > max_value:
        max_value = new_integer
        update_count += 1
        print(f"{new_integer} (New Maximum)")
    else:
        print(new_integer)

print(
    f"The maximum value total is {max_value}, and it was changed {update_count} times."
)


# 3) Greatest Common Divisor #######################################################################

import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

result = gcd(num1, num2)
print(f"The GCD is {result}")


# 4) Binary To Decimal ##############################################################################


def binary_to_decimal(binary_str):
    decimal = 0
    for digits in binary_str:
        decimal = decimal * 2 + int(digits)
    return decimal


binary_input = input("enter binary: ")
decimal_output = binary_to_decimal(binary_input)
print(decimal_output)


# 5) Decimal To Binary ####################################################################################


def decimal_to_binary(decimal):
    binary = ""

    if decimal == 0:
        return "0"

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2

    return binary


decimal = int(input("Enter a decimal number: "))


binary = decimal_to_binary(decimal)
print(f"the binary number is: {binary}")
