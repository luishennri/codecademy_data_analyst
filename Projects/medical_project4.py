names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append('Priscilla')
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))
num_medical_records = len(medical_records)
print(f"{num_medical_records}\n")

first_medical_record = medical_records
print(f"Here is the frist medical record: {first_medical_record}\n")

first_medical_record.sort()
print(f"Here are the medical records sorted by insurance cost: {first_medical_record}\n")

cheapest_three = first_medical_record[0:3]
print(f"Here are the three cheapest insurance costs in our medical records: {cheapest_three}\n")

priciest_three = first_medical_record[-3:]
priciest_three.sort(reverse=True)
print(f"Here are the three most expensive insurance costs in our medical records: {priciest_three}\n")

occurrences_paul = names.count("Paul")
print(f"There are {occurrences_paul} individuals with the name Paul in our medical records.\n")
