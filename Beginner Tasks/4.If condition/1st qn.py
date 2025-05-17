def calculate_BMI(weight,height):
    bmi=weight/(height*height)
    return bmi
height=float(input("Enter the height in meters"))
weight=int(input("Enter the weight"))
bmi=calculate_BMI(weight,height)
if bmi>=30:
    print("Obesity")
elif bmi>=18.5 and bmi<=25:
    print("Normal")
else:
    print("Underweight")