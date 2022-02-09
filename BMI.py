def CalculateTdeeMen():
    BMR = 10 * WEIGHT + 6.25 * HEIGHT - 5 * AGE + 5
    return BMR


def CalculateTdeeWomen():
    BMR = 10 * WEIGHT + 6.25 * HEIGHT - 5 * AGE - 161
    return BMR


def CalculateBMI():
    if BMI < 18.5:
        return "under weight"
    elif 18.5 <= BMI <= 24.9:
        return "normal weight"
    elif 25 <= BMI <= 29.9:
        return "over weight"
    elif BMI > 30:
        return "obese"


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
print("")

if ACTIVITY == 1:
    tdee = MINI
elif ACTIVITY == 2:
    tdee = LIGHT
elif ACTIVITY == 3:
    tdee = MODERATE
elif ACTIVITY == 4:
    tdee = ACTIVE
elif ACTIVITY == 5:
    tdee = EXTRA

BMI = (WEIGHT / HEIGHT / HEIGHT) * 10000

body = CalculateBMI()
print("Your BMI is: {}. Which makes you {}".format(round(BMI, 1), body))

if GENDER == "M":
    print("Your BMR is: {}".format(CalculateTdeeMen()))
    print("TDEE: ", round(CalculateTdeeMen() * tdee))
else:
    print("Your BMR is: {}".format(CalculateTdeeWomen()))







