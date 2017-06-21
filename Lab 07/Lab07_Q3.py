
# Lab 07 - Problem 03

def Tuition_instate(credit):


    if credit > 12:

        credit = 12

    cost  = 60 * credit

    print("You are paying in-state rate")
    print("Please pay $",cost)

def Tuition_outstate(credit):

    if credit > 15:

        credit = 15

    cost = 200 * credit

    print("You are paying out-of-state rate")
    print("Please pay $",cost)

def main():

    state = str(input("Are you in-state student?[y/n] "))
    credit = float(input("How many credit hours are you taking?"))

    if state == 'y':

        Tuition_instate(credit)

    elif state == 'n':

        Tuition_outstate(credit)

main()
