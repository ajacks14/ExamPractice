import random

# y=0
# for x in range(5):
#     y+=1
#     print("\n")
#     for x in range(1,11):
#         print(x*y, end=" ")


randomno= random.randint(0,99)
print(randomno)
noguesses = 0

correct = False

while not correct:
    inputs = int(input("guess a no between 0 - 99: "))
    noguesses += 1
    if inputs < randomno:
        print(" too low. guess again ")
    elif inputs > randomno:
        print(" too high. guess again ")
    else:
        print("correct. it took you ", noguesses,  " guesses ")
        correct = True