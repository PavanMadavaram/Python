#Day 24 - BMI Calculator
weight = 65  # kg
height = 1.7 # meters

bmi = weight / (height * height)
print("Your BMI:", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
else:
    print("Overweight")
