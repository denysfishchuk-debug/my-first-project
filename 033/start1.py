def greet_ilp_participant():
    print("Hello ILP participant!")

greet_ilp_participant()


def greet_person(name):
    print(f"Hello {name}!")

greet_person("Denis")


def calculate_product(a, b):
    return a * b

result = calculate_product(6, 7)
print("Product:", result)



def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

bmi1 = calculate_bmi(70, 1.75)
bmi2 = calculate_bmi(85, 1.82)

print("BMI 1:", round(bmi1, 2))
print("BMI 2:", round(bmi2, 2))


def find_min_max(numbers):
    return min(numbers), max(numbers)

my_list = [3, 7, 1, 9, 4, 2]
minimum, maximum = find_min_max(my_list)

print("Min", minimum)
print("Max", maximum)
