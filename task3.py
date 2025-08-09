import random
import string
while(True):
    n=int(input("please enter number greater than 4: "))
    password_list=[]
    if n>=4:
        for i in range(4):
            if i == 0:
                random_letter=random.choice(string.ascii_uppercase)  # Uppercase
            elif i == 1:
                random_letter=random.choice(string.ascii_lowercase)  # Lowercase
            elif i == 2:
                random_letter=random.choice(string.digits)           # Digit
            elif i == 3:
                random_letter=random.choice(string.punctuation)      # Special char
            password_list.append(random_letter) 

        for i in range(4,n):
            pick = random.randint(1, 4)
            if pick == 1:
                random_letter = random.choice(string.ascii_uppercase)
            elif pick == 2:
                random_letter = random.choice(string.ascii_lowercase)
            elif pick == 3:
                random_letter = random.choice(string.digits)
            elif pick == 4:
                random_letter = random.choice(string.punctuation)  
            password_list.append(random_letter) 
        random.shuffle(password_list)
        print(password_list)
    else:
        print("size must be greater than 4")