import csv

with open('codecademy_data_analyst/us-medical-insurance-costs/insurance.csv', 'r') as insurance_csv_file:
    csv_reader = csv.reader(insurance_csv_file)

    for row in csv_reader:
        print(row)
        