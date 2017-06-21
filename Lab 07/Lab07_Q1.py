# Lab 07 - Problem 01

def calc_bmi():

    height = float(input("Enter height (in inches):"))
    weight = float(input("Enter weight (in pounds):"))

    bmi = (703 * weight) / (height*height)

    print("Your BMI is:", bmi,"\n")

def hypertension():

    systolic_p = float(input("Enter your systolic pressure:"))
    diastolic_p = float(input("Enter your diastolic pressure:"))

    if systolic_p >= 140 or diastolic_p >=90:

        print("You have high blood pressure.")

    else:

        print("You do not have high blood pressure.")

def main():

    print("Health and Fitness Program\n")

    calc_bmi()
    hypertension()



main()
