import random
names = "Alex Beth Caroline Dave Ellen Mike".split()

scores = {name:random.randint(1,100) for name in names}

print(scores)
