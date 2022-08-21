import random
import math

# taking the inputs
lower = int(input("Enter Lower Number: "))
upper = int(input("Enter Upper Number: "))

# generating random numbers
x = random.randint(lower, upper)
print("\n\tYou Have Only ",round(math.log(upper - lower + 1, 2)), " chances to guess the number!\n")

# initial the guess
count = 0

# for guessing the minimum number of guesses depends of choosen range
while count <math.log(upper - lower + 1, 2):
    count += 1
    
    # take guessing numbers as inputs
    guess = int(input("Enter Guess Number: "))
    
    # condition checking
    if x == guess:
        print("Congratulations... You have guessed it in ",count, " try")
        
        # once guessed correctly loop will break
        break
    elif x > guess:
        print("your guessed is too small!!")
    elif x < guess:
        print("your guessed is too high!!!")
        
# If Guessing is more than required guesses, show this output
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
