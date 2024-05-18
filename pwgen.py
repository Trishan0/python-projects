import random
import string

print("This is a Small Password Genrator")

#Declare the variables
letters = string.ascii_letters
symbols = string.punctuation
digits = string.digits
password = []

count = 0
count1= 0
count2 = 0


##Ask for user inputs and check the character length is less than 8
while True:
    count = count1 = count2 = 0
    while count <= 0 :
        count = int(input("How many letters would you like in your password ? "))
    while count1 <= 0 :
        count1 = int(input("How many Symbols would you like in your password ? "))
    while count2 <= 0 :
        count2 = int(input("How many Digits would you like in your password ? "))

    if count+count1+count2 >= 8:
        break
    else:
        print("password is too short ! Please try Again !")
     

for _ in range(count):              #Generate random letters
    password.append(random.choice(letters))
    
for _ in range(count1):             #Generate random Numbers
    password.append(random.choice(digits))
    
for _ in range(count2):             #Generate random Symbols
    password.append(random.choice(symbols))

random.shuffle(password)            #Shuffle the password
#password1 = [print(i,end="") for i in password]   #print the password using list comprehension
print("".join(password),"\nthis is the 1nd password \n")     #convert the list into a string & print it