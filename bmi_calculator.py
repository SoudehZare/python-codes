print("this is BMI generator... ")
height = float(input("give me your height in M: "))
weight = float(input("give me your weight in kg: "))
BMI= (weight/(height ** 2))
print(BMI)

if BMI <= 18.5:
    print('underweight')
elif BMI <= 25:
    print('normal')
elif BMI <= 35:
    print('Overweight')
elif BMI <= 45:
    print('obesity')
else:
     print("BMI is not correct")
