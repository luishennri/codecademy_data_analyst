import csv

# Open the csv file and separating by column.
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []
with open('codecademy_data_analyst/us-medical-insurance-costs/insurance.csv', 'r') as insurance_csv_file:
    csv_reader = csv.DictReader(insurance_csv_file)
    for column in csv_reader:
        age.append(column['age'])
        sex.append(column['sex'])
        bmi.append(column['bmi'])
        children.append(column['children'])
        smoker.append(column['smoker'])
        region.append(column['region'])
        charges.append(column['charges'])


# Client class  
smoker_x = '' 
class client:
    def __init__(self, age, sex, bmi, children, smoker, region, charges):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = region
        self.charges = charges
    
    def __str__(self) -> str:
        if self.smoker == 'yes':
            smoker_x == 'smoker'
        else:
            smoker_x == 'non-smoker'

        return(f"This client is a {self.sex} with {self.age} years old, have {self.children} children, live in {self.region} region, the body mass index is {self.bmi}, is a {smoker_x} and the insurance cost is {self.charges}")

# Creating the clients
client_dict = {}

for i in range(len(age)):
    client(age[i], sex[i], bmi[i], children[i], smoker[i], region[i], charges[i])
    client_dict[i] = {'age': age[i], 'sex': sex[i], 'bmi': bmi[i], 'children': children[i], 'smoker': smoker[i], 'region': region[i], 'charges': charges[i]}

for id, person in client_dict.items():
    print(id, person)

# Find out the average age of the patients in the dataset.
average_age = 0

def average_by_age(ages):
    sum = 0
    for age in ages:
        sum += int(age)
    average_age = sum / len(ages)
    return average_age

print(f'\nThe average of ages is {round(average_by_age(age), 2)}.\n')

# Analyze where a majority of the individuals are from.
majority_are_from = ''

def where_majority_are_from(regions):
    each_reagion = []
    count = 0
    for region in regions:
        if region not in each_reagion:
            each_reagion.append(region)

    for reagion_name in each_reagion:
        if count < regions.count(reagion_name):
            count = regions.count(reagion_name)
            majority_are_from = reagion_name
    
    return f'The region with the marority of infividuals are {majority_are_from} with {count} people from {len(regions)}.\n'

print(where_majority_are_from(region))

# The different costs between smokers vs. non-smokers.
smokers_and_cost = list(zip(smoker, charges))
smoker_difference = 0


def difference_by_smoker(list):
    sum_smokers = 0
    sum_no_smokers = 0

    for item in list:
        if item[0] == 'yes':
            sum_smokers += float(item[1])
        else:
            sum_no_smokers += float(item[1])
    smoker_difference = abs(sum_smokers - sum_no_smokers)

    return f'''The total paid by smokers is {round(sum_smokers, 2)}$ and by non-smokers is {round(sum_no_smokers, 2)}$ almost the same. 
Therefore, the diffence between smoker and non-smoker is {round(smoker_difference, 2)}$ paid by non-smokers. 
But the number of non-smokers is {round(smoker.count('no') / smoker.count('yes'), 2)} times bigger than smokers. 
'''

print(difference_by_smoker(smokers_and_cost))

# The average age is for someone who has at least one child in this dataset.

age_and_children = list(zip(age, children))

def parents_average_age(list):
    ages = []
    for item in list:
        if int(item[1]) > 0:
            ages.append(item[0])
    average =  round(average_by_age(ages), 0)

    return f'The average for people who have children is {int(average)} years olds.\n'

print(parents_average_age(age_and_children))

# The average bmi is for someone who is a smoker.
bmi_and_smoker = list(zip(bmi, smoker))
bmi_average_smoker = 0
def bmi_smoker(list):
    smokers = []
    count = 0
    for item in list:
        if item[1] == 'yes':
            count += float(item[0])
            smokers.append(item[1])
    bmi_average_smoker = count / len(smokers)
    return f'The bmi average of a smoker is {round(bmi_average_smoker, 2)}'

print(bmi_smoker(bmi_and_smoker))
