# 1) #######################################################

word = input("Input a word: ")
vowels = ["a", "e", "i", "o", "u"]
vowelnum = 0
word = word.lower()

for char in word:
    if char in vowels:
        vowelnum += 1

print(f"You have {vowelnum} vowels in that word.")


# 2)  #######################################################

while True:
    cityname = input("Input a city name or nope to stop: ")
    if cityname.lower() == "nope":
        break
    print(f"Oh! {cityname} is a cool spot.")

print("bye")


# 3  #######################################################
sum = 0
num_amt = 0
while True:
    number = int(input("input a number: "))
    num_amt += 1
    sum = sum + number
    if sum >= 200:
        print(f"sum = {sum}")
        print(f"numbers entered: {num_amt}")
        break
# 4  #######################################################

num = 35
print(num)
for x in range(10):
    num += 1
    print(num)

# 5 #######################################################

num = 350
print(num)
for x in range(50):
    num += 2
    print(num)

# 6 #######################################################

age_sum = 0.0
for x in range(7):
    age = float(input(f"Enter age {x + 1}: "))
    age_sum += age

print(f"The sum of the  ages is: {age_sum}")
