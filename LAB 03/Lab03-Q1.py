
midterm_score = float(input("Enter midterm score:"))
final_score = float(input("Enter final score:"))

score = midterm_score + 20

if final_score >= score:
    print("5 bonus points added to total for meeting improvement target:")
    total = midterm_score + final_score + 5
    print("New total score:", total)

elif final_score != score:
    total = midterm_score + final_score
    print("Total score:",total)
