import random
import time as t
# EXCERSISE NUMBER 1

num = int(input("please input a number: "))
num_even = num % 2
if num_even == 0:
    print("this number is even")
else:
    print("this number is odd")

# EXCERSISE NUMBER 2

letter = input("please input a letter: ")
letter = letter.lower()

if len(letter) == 1:
    if letter in ["a", "e", "i", "o", "u"]:
        print("this is a vowel")
    elif letter == "y":
        print("y is a vowel but can sometimes be a consonant")
    else:
        print("this is a consonant")
else:
    print("thats not a letter stupid")

# EXCERSISE NUMBER 3

magnitudes = {
    (float("inf"), 2): "micro",
    (2, 3): "very minor",
    (3, 4): "minor",
    (4, 5): "light",
    (5, 6): "moderate",
    (6, 7): "strong",
    (7, 8): "major",
    (8, 10): "great",
    (10, float("inf")): "meteoric",
}


question = float(
    input("please inpute an earthquake magnitude and ill tell you how bad it is: ")
)

for number, value in magnitudes.items():
    if number[0] <= question < number[1]:
        magnitude_name = value
        break
if magnitude_name:
    print(f"a magnitude {question} is a {magnitude_name} earthquake")

# EXCERSISE NUMBER 4

base_charge = 15
given_minutes = 50
given_messages = 50
minute_rate = 0.25
message_rate = 0.15
nine_one_one_call = 0.44
sales_tax = 0.05
extra_minutes = 0
extra_messages = 0

minutes_used = float(input("please input the number of minutes used: "))
messages_used = float(input("please input the number of messages sent: "))

if minutes_used > 50:
    extra_minutes = minutes_used - 50
    extra_minutes = extra_minutes * 0.25

if messages_used > 50:
    extra_messages = messages_used - 50
    extra_messages = extra_messages * 0.25

subtotal = extra_minutes + extra_messages + nine_one_one_call + base_charge
tax = subtotal * sales_tax
bill = subtotal + tax

print(f"your total bill is ${bill:0.2f}")

# EXCERSISE NUMBER 5


red_numbers = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
spin_result = random.randint(0, 36)
print(f"The spin was {spin_result}")
if spin_result == 0:
    print("Pay 0")
elif spin_result == 00:
    print("Pay 00")
else:
    print("Pay", spin_result)
    if spin_result in red_numbers:
        print("Pay Red")
    else:
        print("Pay Black")
    if spin_result % 2 == 0 and spin_result not in [0, 00]:
        print("Pay Even")
    elif spin_result % 2 != 0 and spin_result not in [0, 00]:
        print("Pay Odd")
    if 1 <= spin_result <= 18:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")
