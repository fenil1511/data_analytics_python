from pickle import HIGHEST_PROTOCOL
grades = [
    ["Fenil", "Python", 85],
    ["Ankit", "Python", 92],
    ["Rahul", "SQL", 78],
    ["Priya", "Python", 95],
    ["Karan", "SQL", 64],
    ["Sonia", "Python", 88]
]

# add new value in grades list 
grades.append(["Meera", "Python", 90])

# add values in list 
name = []
sub=[]
scores = []
for item in grades :
    name.append(item[0])
    sub.append(item[1])
    scores.append(item[2])


total_students = len(scores)
average_scores = sum(scores)
highest_score = max(scores)
lowest_score = min(scores)

# print(f"Total Students: {total_students}")
# print(f"Average Scores : {average_scores:.2f}")
# print(f"Highest Score:  {highest_score}")
# print(f"Lowest Score:   {lowest_score}")

# Filter top performers
# top_performers = [p for p in scores if p >= 85 ]
# # print(top_performers)

top_performers = []

for students in grades:
    name = students[0]
    score = students[2]

    if score >= 85: 
        top_performers.append(f"{name} ({score})")


for item in top_performers:
    print(item)



