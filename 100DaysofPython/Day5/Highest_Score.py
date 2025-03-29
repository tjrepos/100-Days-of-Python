student_scores = [180, 124, 165, 173, 189, 169, 146]

print(max(student_scores))

high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score

print(high_score)
