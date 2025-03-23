# BMI Calculator script

print("Welcome to the BMI Calculator!!")
height = float(input("Please enter your height in metres: "))
weight = float(input("Please enter your weight in kilograms: "))

bmi = weight / (height ** 2)

print(f"""With a height of {height} meters and a weight of {weight} kilograms, your BMI is {round(bmi, 1)}
""")

if bmi < 18.5:
    print("You should consider gaining some weight as you are underweight!")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Well done. You are at a healthy weight.")
elif bmi >= 25 and bmi <= 29.9:
    print("You are a bit overweight. Eat less snacks!")
elif bmi >= 30 and bmi <= 34.9:
    print("You are Obese Class I. Time to start making an effort to lose weight!!")
elif bmi >=35 and bmi <= 39.9:
    print("You are Obese Class II. PUT DOWN THE CUPCAKE!!")
elif bmi >= 40:
    print("You are Obese Class III. Seek medical help now!!!")
optimal_bmi_min = 18.5
optimal_bmi_max = 24.9
ideal_weight_min = optimal_bmi_min * (height ** 2)
ideal_weight_max = optimal_bmi_max * (height ** 2)
print(f"Based on your height and an optimal BMI range of {optimal_bmi_min} - {optimal_bmi_max},\nyour ideal weight range is between {round(ideal_weight_min)} and {round(ideal_weight_max)} kgs.")