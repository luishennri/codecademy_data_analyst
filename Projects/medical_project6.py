medical_data = \
    """Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

## replace # for $ 
updated_medical_data = medical_data.replace('#', '$')

## counting the number of insurance costs in the list
num_records = 0
for i in updated_medical_data:
    if i == '$':
        num_records += 1


print(f'There are {num_records} medical records in the data.num_records\n')

## spliting the data
medical_data_split = updated_medical_data.split(';')

## spliting the data in each record
medical_records = []
for record in medical_data_split:
    medical_records.append(record.split(','))

## cleaing the data, removing the blank spaces
medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())

    medical_records_clean.append(record_clean)

for record in medical_records_clean:
  print(record[0].upper().upper())

## append each record in separate lists
names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

print(f'\n{names}\n {ages}\n {bmis}\n {insurance_costs}\n')

## calculating the total and avarege of bmi
total_bmi = 0

for bmi in bmis:
    total_bmi += float(bmi)

average_bmi = round(total_bmi / len(bmis), 2)

## calculating the total and avarege of insurance costs
total_insurance_costs = 0
for insurance_cost in insurance_costs:
    clean_insurance_costs = []
    clean_insurance_costs.append(insurance_cost.strip('$'))
    for insurance_cost in clean_insurance_costs:
        total_insurance_costs += float(insurance_cost)

average_insurance_costs = round(total_insurance_costs / len(insurance_costs))

print('BMI avarege: ' + str(average_bmi))
print('\nInsurance costs avarege: $' + str(average_insurance_costs))


for i in range(0,len(names)):  
    print(f'\n'+ names[i] + ' is '+ ages[i] + ' years old with a BMI of ' + bmis[i] +  ' and an insurance cost of $' + insurance_costs[i] + '.')








