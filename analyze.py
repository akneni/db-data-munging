import csv
# Place code below to do the analysis part of the assignment.


# We need to find the
# Average anomalies from 1880-1889
# Average anomalies from 1890-1899
# etc

# Grab data from csv file
with open('./data/clean_data.csv', 'r') as f:
    data = list(csv.DictReader(f))

# first element of each value in the dict is the running sum and the second is 
# there to track the number of years in each decade (since we only have 3 years of data for
# the decade of 2020)
decade_means = {
    '1880': [0, 0],
    '1890': [0, 0],
    '1900': [0, 0],
    '1910': [0, 0],
    '1920': [0, 0],
    '1930': [0, 0],
    '1940': [0, 0],
    '1950': [0, 0],
    '1960': [0, 0],
    '1970': [0, 0],
    '1980': [0, 0],
    '1990': [0, 0],
    '2000': [0, 0],
    '2010': [0, 0],
    '2020':[0, 0]
}

# Sum up the total for each decade
for year in data:
    # Replace the last digit of the year with zero
    decade = year['Year'][:-1] + "0"

    decade_means[decade][0] += int(year['J-D'])
    decade_means[decade][1] += 1

# Divide the running total for each decade by the number of entries for that decade
for k, v in decade_means.items():
    decade_means[k] = v[0] / v[1]


# print out average means
print("""
Note: each key represents the decade starting at that year. 
For example, "1880" represent the decade "1880-1889".
""".strip())
print(decade_means)

