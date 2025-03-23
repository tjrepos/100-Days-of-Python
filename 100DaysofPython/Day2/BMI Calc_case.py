# BMI Calculator script
import sys

print("Welcome to the BMI Calculator!!")
height = float(input("Please enter your height in metres: "))
weight = float(input("Please enter your weight in kilograms: "))

bmi = float(round(weight / (height ** 2), 2))

print(f"""With a height of {height} meters and a weight of {weight} kilograms, your BMI is {bmi}
""")


match bmi:
    case < 18.5:
        print("You should consider gaining some weight as you are underweight!")
    case < 25:
        print("Well done. You are at a healthy weight.")
    case < 30:
        print("You are a bit overweight. Eat less snacks!")
    case < 35:
        print("You are Obese Class I. Time to start making an effort to lose weight!!")
    case < 40:
        print("You are Obese Class II. PUT DOWN THE CUPCAKE!!")
    case >= 40:
        print("You are Obese Class III. Seek medical help now!!!")
    case _:
        print("Error!!! The world will now end!!!")

optimal_bmi_min = 18.5
optimal_bmi_max = 24.9
ideal_weight_min = optimal_bmi_min * (height ** 2)
ideal_weight_max = optimal_bmi_max * (height ** 2)
print(f"Based on your height and an optimal BMI range of {optimal_bmi_min} - {optimal_bmi_max},\n your ideal weight range is between {round(ideal_weight_min)} and {round(ideal_weight_max)} kgs.")