# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight / height**2)

limits = [18.5, 25, 30, 35]
wording = ["underweight", "normal weight",
           "slightly overweight", "obese", "clinically obese"]

selection = None
for i in range(len(limits)):
    if bmi < limits[i]:
        selection = wording[i]
        break
if not selection:
    selection = wording[-1]

print(f"Your BMI is {bmi}, you are {selection}.")
