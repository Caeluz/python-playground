import numpy as np
import random
import sklearn as sk

guess_right = 0
guess_wrong = 0
ranges = 1
for i in range(ranges):
    predictions = random.randint(0, 1)
    guess = random.randint(0, 1)

    if predictions == guess:
        print(True)
        guess_right += 1
    else:
        print(False)
        guess_wrong += 1

print("Guess right: ", guess_right/ranges * 100, "%")
print("Guess wrong: ", guess_wrong/ranges * 100, "%")
