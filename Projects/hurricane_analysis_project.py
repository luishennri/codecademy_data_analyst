# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah',
         'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma',
         'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September',
          'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October',
          'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005,
         2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175,
                       165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles',
                                                                  'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], [
                      'The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], [
    'Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
    ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], [
        'The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
    ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], [
        'Mexico'], ['The Caribbean', 'United States East coast'],
    ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela',
                                                                     'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'],
    ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula',
                                                             'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
    ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands',
                                                                 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
    ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America',
                                           'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
    ['Antilles', 'Venezuela', 'Colombia',
        'United States East Coast', 'Atlantic Canada'],
    ['Cape Verde', 'The Caribbean', 'British Virgin Islands',
        'U.S. Virgin Islands', 'Cuba', 'Florida'],
    ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M',
           'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11,
          2068, 269, 318, 107, 65, 19325, 51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
updated_damages = []

x = 0


def updating_damages(damages, conversion):

    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        else:
            if damage[-1] == 'M':
                x = float(float(damage[0:-1]) * conversion['M'])
                updated_damages.append(x)
            else:
                x = float(float(damage[0:-1]) * conversion['B'])
                updated_damages.append(x)
    return updated_damages


print(updating_damages(damages, conversion))
# 2
# Create a Table
# Create and view the hurricanes dictionary
hurricanes_by_name_completed = {}
hurricanes_in_process = {}


def hurricanes_by_name(names, months, years, max_winds, areas, damages, deaths):
    for i in range(0, len(names)):
        hurricanes_in_process = {'Name': names[i], 'Month': months[i], 'Year': years[i],
                                 'Max Sustained Wind': max_winds[i], 'Areas Affected': areas[i], 'Damage': damages[i], 'Deaths': deaths[i]}
        hurricanes_by_name_completed[names[i]] = hurricanes_in_process
    return hurricanes_by_name_completed


print('\n')
print(hurricanes_by_name(names, months, years,
      max_sustained_winds, areas_affected, damages, deaths))

# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key
hurricanes_by_year_completed = {}


def hurricanes_by_year(years, hurricanes):
    last_year = 0
    for year in years:
        auxiliary = []
        last_year = year
        for item in hurricanes:
            if year == hurricanes[item]['Year']:
                hurricanes_by_year_completed.update({year: hurricanes[item]})
                if last_year == year:
                    auxiliary.append(hurricanes[item])
                    hurricanes_by_year_completed.update({year: auxiliary})
                else:
                    auxiliary.append(hurricanes[item])

    return hurricanes_by_year_completed


print('\n')
hurricanes_by_year(years, hurricanes_by_name_completed)
for i in hurricanes_by_year_completed:
    print(f'{i} {hurricanes_by_year_completed[i]}')

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in
hmt_areas_affected_completed = {}


def hmt_areas_affected(areas_effected):
    auxiliary = []
    for areas in areas_effected:
        for area in areas:
            auxiliary.append(area)

    for area in auxiliary:
        count = auxiliary.count(area)
        hmt_areas_affected_completed[area] = count

    return hmt_areas_affected_completed


print('\n')
print(hmt_areas_affected(areas_affected))

# 5
# Calculating Maximum Hurricane Count
# find most frequently affected area and the number of hurricanes involved in
max_area_count_completed = {}


def affected_areas_count(ares_times):
    max_area = ''
    max_area_count = 0
    for area, times in ares_times.items():
        if max_area_count < times:
            max_area = area
            max_area_count = times
        max_area_count_completed[max_area] = max_area_count

    return max_area_count_completed


print('\n')
print(affected_areas_count(hmt_areas_affected_completed))

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths

max_deadliest_count_completed = {}


def deadliest_count(deaths):
    max_deaths = max(deaths)
    for name, items in hurricanes_by_name_completed.items():
        for category, values in items.items():
            if category == 'Deaths' and values == max_deaths:
                max_deadliest_count_completed[name] = max_deaths
    return max_deadliest_count_completed


print('\n')
print(deadliest_count(deaths))

# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
hurricanes_by_mortality_completed = {}

def hurricanes_by_mortality(hurricanes, scales):
    for name, hurricane in hurricanes.items():
        for category, item in hurricane.items():
            if category == 'Deaths':
                for scale, deaths in scales.items():
                    if item >= deaths:
                        hurricanes_by_mortality_completed[name] = scale
    return hurricanes_by_mortality_completed

print('\n')
print(hurricanes_by_mortality(hurricanes_by_name_completed, mortality_scale))

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost



# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

# categorize hurricanes in new dictionary with damage severity as key
