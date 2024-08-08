import random

print("██████   █████  ███████ ███████      ██████  ███████ ███    ██ ███████ ██████   █████  ████████  ██████  ██████  ")
print("██   ██ ██   ██ ██      ██          ██       ██      ████   ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ ")
print("██████  ███████ ███████ ███████     ██   ███ █████   ██ ██  ██ █████   ██████  ███████    ██    ██    ██ ██████  ")
print("██      ██   ██      ██      ██     ██    ██ ██      ██  ██ ██ ██      ██   ██ ██   ██    ██    ██    ██ ██   ██ ")
print("██      ██   ██ ███████ ███████      ██████  ███████ ██   ████ ███████ ██   ██ ██   ██    ██     ██████  ██   ██ ")
print("                                                                                                                 ")
                                                                                                                 

length = int(input("\nEnter password length: "))
name = input("\nEnteryourname: ")

characterList = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password = []

for i in range(length):
   
    randomchar = random.choice(characterList)
   
    password.append(randomchar)
 
print("The random password is ", name + "".join(password))
