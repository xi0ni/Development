"""#steps for the algorithm:

1. remove every third character unless its the last letter
2. Capitalize every alternate letter
3.double the first and last letters
4.reverse the middle section (everything but the first and last letters)
5. substitute all e's with 3
6. add a special character based on the website purpose.
(education is &, entertainment is !, social media is #, online shop is $)

instagram
IMaRaTnIM#
"""

"""


pseudocode:
    
website = the input from the user
choice = the four choices that determine the special character

1.
define capitalize alternate letters:
    for letters in word:
        if length of letter % 2 = 0:
            capitalize
2.
for 'e' in website:
    if e is in word:
        change word to 3
3.
    if letter % 3 = 1:
        remove the letter


4.
for characters in website:
    choice = random.choice(1,2)
    if the coice = 1:
        upper
    else:
        lower
5.
  first letter = word[0]
last letter = word[-1]
first letter *2
last letter*2

6.
if choice = a:
    add &
elif choice = b:
    add !
elif choice = c:
    add #
else:
    add $
    
    """

"""final code:"""

website = input("tell me the website you need a password for: ")
choice = input(
    "tell me the function of the website:\n a.education \n b.entertainment \n c.social media \n d.online shop \n "
)


def password_gen(word):
    # 1. Remove every third letter
    result = ""
    n = 1
    for ch in word:
        if n % 3 != 0:
            result += ch
        n += 1
    # 2. Replace e with 3
    result = result.replace("e", "3")
    # 3. Capitalize alternate letters
    final_result = ""
    for index, letter in enumerate(result):
        if index % 2 == 0:
            final_result += letter.upper()
        else:
            final_result += letter.lower()
    # 5. duplicate the first and last letters and reverse the middle section
    first_letter = word[0]
    last_letter = word[-1]
    reverse = final_result[::-1]
    duplicated_string = first_letter + reverse + last_letter

    # 6. write a symbol based on the input of choice
    if choice == "a" or choice == "A":
        duplicated_string = duplicated_string + "&"
    elif choice == "b" or choice == "B":
        duplicated_string = duplicated_string + "!"
    elif choice == "c" or choice == "C":
        duplicated_string = duplicated_string + "#"
    else:
        duplicated_string = duplicated_string + "$"

    return duplicated_string


result = password_gen(website)
print(result)
