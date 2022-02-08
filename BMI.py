MINI = 1.2
LIGHT = 1.375
MODERATE = 1.550
ACTIVE = 1.725
EXTRA = 1.9

GENDER = input("Enter gender M/F: ")
WEIGHT = int(input("Enter your weight: "))
HEIGHT = int(input("Enter your height (cm): "))
AGE = int(input("Enter your age: "))
print("")
print("Little or no exercise: 1\nLight Exercise (3-5 days a week): 2\nModerate Exercise (3-5 days a week): 3\nHard "
      "Exercise (6-7 days a week): 4\nExtra Hard Exercise (Sports 6-7 days a week): 5\n")
ACTIVITY = int(input("Choose Activity Level 1-5: "))

BMI = (WEIGHT / HEIGHT / HEIGHT) * 10000

def CalulateActivity():


def CalculateTdeeMen():
    BMR = 10 * WEIGHT + 6.25 * HEIGHT - 5 * AGE + 5
    return BMR


def CalulateTdeeWomen():
    BMR = 10 * WEIGHT + 6.25 * HEIGHT -5 * AGE - 161
    return BMR

def CalulateBMI(BMI):
    if BMI < 18.5:
        return "Under weight"
    elif 18.5 <= BMI <= 24.9:
        return "Normal weight"
    elif 25 <= BMI <= 29.9:
        return "Over weight"
    elif BMI > 30:
        return "Obese"


body = CalulateBMI(BMI)
print("Your BMI is: {}. Which makes you {}".format(round(BMI, 1), body))

if GENDER == "M":
    print("Your BMR is: {}".format(CalculateTdeeMen()))
else:
    print ("Your BMR is: {}".format(CalulateTdeeWomen()))





