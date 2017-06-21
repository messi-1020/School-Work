
 # Lab 07 - Problem 05

def main():

    score_list = []

    i = 0

    while i != 5:

        score = float(input("Enter a score: "))

        score_list.append(score)

        i = i + 1

    avg_score = sum(score_list) / len(score_list)

    print("The average score is", avg_score)

main()
