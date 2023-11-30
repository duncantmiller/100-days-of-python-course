import random
names = "Alex Beth Caroline Dave Ellen Mike".split()

scores = {name:random.randint(1,100) for name in names}

passed_scores = {record for record in scores if scores[record] > 75}

print(scores)
print(passed_scores)
