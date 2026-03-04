import random

# Function to pick one character from each group
def pick_one_from_each_group(lower_case, upper_case, numbers, symbols):
    lower = random.choice(lower_case)
    upper = random.choice(upper_case)
    num = random.choice(numbers)
    sym = random.choice(symbols)
    
    return [lower, upper, num, sym]

# Character lists
lower_case = ['a','b','c','d','e','f','g','h','i']
upper_case = ['A','B','C','D','E','F','G','H','I']
numbers = ['1','2','3','4','5','6','7']
symbols = ['$', '*', '#', '@', '&', '%']

all_characters = lower_case + upper_case + numbers + symbols

print("---- Password Generator ----")

# Get password length
length = int(input("Enter Password length: "))

# Check minimum length
if length < 4:
    print("Length must be 4 or greater!")
else:
    # Get one character from each group
    password_chars = pick_one_from_each_group(lower_case, upper_case, numbers, symbols)
    
    # Add remaining characters randomly
    for _ in range(length - 4): #Length -4 because we alreday take 4 characters
        password_chars.append(random.choice(all_characters))
    
    # Shuffle to randomize order
    random.shuffle(password_chars)
    
    # Convert list to string
    password = "".join(password_chars)
    
    # Print final password
    print("Generated Password is:", password)