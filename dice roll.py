import random
min_value= 1
max_value= 6
roll_again="yes"
while roll_again=="yes" or roll_again=="y":
    print("rolling the dice")
    print("the value is")
    print(random.randint(min_value,max_value))
    roll_again= input("roll the dice again: ")  