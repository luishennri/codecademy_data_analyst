medical_costs = {}
medical_costs.update({'Maria': 6607.0, 'Vinay': 3225.0})
medical_costs.update({'Connie': 8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0})
medical_costs['Vinay'] = 3325.0

total_costs = 0
for value in medical_costs.values():
    total_costs += value

average_cost = total_costs / len(medical_costs)

names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]

zipped_ages = list(zip(names, ages))

names_to_ages = {key: value for key, value in zipped_ages}

marina_age = names_to_ages.get('Marina')
print(f'Marina age is {marina_age}.')

medical_records = {}

medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1,
                             "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9,
                            "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3,
                             "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6,
                            "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7,
                                "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(
    f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars.")

medical_records.pop("Vinay")


def update_medical_records(name, age, sex, bmi, children, smoker, insurance):
    medical_records[name] = {"Age": age, "Sex": sex, "BMI": bmi,
                             "Children": children, "Smoker": smoker, "Insurance_cost": insurance}
    return medical_records


update_medical_records('Luis', '24', 'Male', 20.0, 0, 'Nom-smoker', 5000.0)


def print_medical_record():
    for name, item in medical_records.items():
        print(
            f"{name} is a {item['Age']} year old {item['Sex']} {item['Smoker']} with a BMI of {item['BMI']} and insurance cost of {item['Insurance_cost']}")


print_medical_record()
