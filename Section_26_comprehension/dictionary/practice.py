import random
names = "Alex Beth Caroline Dave Ellen Mike".split()

scores = {name:random.randint(1,100) for name in names}

passed_scores = {key:value for (key, value) in scores.items() if scores[key] > 75}

print(scores)
print(passed_scores)
