# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
def insurance_cost(age, sex, bmi, noc, smoker):
  cost = (250 * age) - (128 * sex) + (370 * bmi) + (425 * noc) + (24000 * smoker) - 12500
  return cost
InsuranceCost = insurance_cost(age, sex, bmi, num_of_children, smoker)
print(f"This person's insurance cost is {InsuranceCost} dollars.\n")

# Age Factor
age += 4
new_insurance_cost = insurance_cost(age, sex, bmi, num_of_children, smoker)
change_in_insurance_cost = new_insurance_cost - InsuranceCost
print(f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost} dollars.\n")

# BMI Factor
age -= 4
bmi += 3.1
new_insurance_cost2 = insurance_cost(age, sex, bmi, num_of_children, smoker)
change_in_insurance_cost2 = new_insurance_cost2 - InsuranceCost
print(f"The change in estimated insurance cost after increasing BMI by 3.1 is {change_in_insurance_cost2} dollars.\n")

# Male vs. Female Factor
bmi -= 3.1
sex = 1
new_insurance_cost3 = insurance_cost(age, sex, bmi, num_of_children, smoker)
change_in_insurance_cost3 = new_insurance_cost3 - InsuranceCost
print(f"The change in estimated cost for being male instead of female is {change_in_insurance_cost3} dollars.\n")

# Extra Practice
sex = 0
num_of_children += 1
new_insurance_cost4 = insurance_cost(age, sex, bmi, num_of_children, smoker)
change_in_insurance_cost4 = new_insurance_cost4 - InsuranceCost
print(f"The change in estimated insurance cost after increasing number of children by 1 is {change_in_insurance_cost4} dollars.\n")

num_of_children -= 1
smoker = 1
new_insurance_cost5 = insurance_cost(age, sex, bmi, num_of_children, smoker)
change_in_insurance_cost5 = new_insurance_cost5 - InsuranceCost
print(f"The change in estimated cost for being no smoker instead a smoker is {change_in_insurance_cost5} dollars.\n")