import pandas

students = {
    "student": "Mike, Joe, Duncan".split(),
    "score": [50, 79, 100]
}

students_df = pandas.DataFrame(students)

for (index, row) in students_df.iterrows():
    if row.student == "Duncan":
        print(row.score)
