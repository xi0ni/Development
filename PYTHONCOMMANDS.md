#Python Commands#



george = [1,2,3,4,5,6,7,8,9,0]
print(george[1::2])
This prints all even numbers in the list. 1 is the starting value and the step is 2
print(george[::-1])
this reverses the order of the list

list comprehension:

new_list = [loop_var for loop_var in iterable]
animals = ["dog" , "cat", "mouse", "frog"]
small_animals = ['small' +i for i in animals]
print(small_animals) 
result:
small dog, small cat, small mouse, small frog

for loops:

for i in range(5,10,2):
    pass
this prints a for loop from 5 -> 10 and it skips every two