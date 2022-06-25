import random
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRRSTUVWXYZ"
number = "0123456789"
specialchar = "@#*&"

all = lowercase + uppercase + number + specialchar
length = 9
password = "".join(random.sample(all,length))
print("your password is : ", password)