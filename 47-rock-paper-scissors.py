rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


# My solution
hand = [rock, paper, scissors]
#p1_throw = random.randint(0,2)
p1_throw = int(input("What do you choose?\n 0 - Rock\n 1 - Paper\n 2 - Scissors\n: "))
p2_throw = random.randint(0,2)

#print(f"P1: {hand[p1_throw]} \nP2 (CPU): {hand[p2_throw]} ")

#print("Solution 1")
if p1_throw >= 3 or p1_throw < 0:
    print("Invalid number")
else:
    print(f"P1: {hand[p1_throw]} \nP2 (CPU): {hand[p2_throw]} ")    

    #if p1_throw == 0 and p2_throw == 0:
    #    print("Result: Draw")
    #elif p1_throw == 1 and p2_throw == 1:
    #    print("Result: Draw")
    #elif p1_throw == 2 and p2_throw == 2:
    #    print("Result: Draw")
    #elif p1_throw == 0 and p2_throw == 1:
    #    print("Result: You lose")
    #elif p1_throw == 1 and p2_throw == 0:
    #    print("Result: You win")
    #elif p1_throw == 2 and p2_throw == 1:
    #    print("Result: You win")
    #elif p1_throw == 0 and p2_throw == 2:
    #    print("Result: You win")
    #elif p1_throw == 1 and p2_throw == 2:
    #    print("Result: You lose")
    #elif p1_throw == 2 and p2_throw == 0:
    #    print("Result: You lose")
    
        
        
    #solution 2
    #print("Solution 2")
    #if p1_throw >= 3 or p1_throw < 0:
    #    print("Invalid number")
    if p1_throw == 0 and p2_throw == 2:
        print("Result: You win")
    elif p1_throw == 2 and p2_throw == 0:
        print("Result: You lose")
    elif p2_throw > p1_throw:
        print("Result: You lose")
    elif p1_throw > p2_throw:
        print("Result: You win")
    elif p1_throw == p2_throw:
        print("Result: Draw")

    