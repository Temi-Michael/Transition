weight = int(input("What is your weight? : "))
height = float(input("What is your height? : "))
BMI = weight / (height * height)
if BMI < 18.5 :
    print(str(BMI) + " is Underweight")
if BMI >= 18.5 and BMI < 25 :
    print(str(BMI) + " is Normal")
if BMI >= 25 and BMI < 30 :
    print(str(BMI) + " is Overweight")
if BMI >= 30 :
    print(str(BMI) + " is Obesity")
