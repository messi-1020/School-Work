
# Lab 07 - Problem 04

def main():

    age = int(input("Enter age: "))
    rest_heart_rate = int(input("Enter resting heart rate: "))

    heart_rate_calculator(age, rest_heart_rate)

def heart_rate_calculator(age, rest_heart_rate):

    target_heart_rate = (220 - age - rest_heart_rate) * 0.4 + rest_heart_rate

    print("Your target heart rate is", target_heart_rate)

main()
