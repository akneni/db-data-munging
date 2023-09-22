import csv

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
    '2020': [0, 0]
}
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Sum up the total for each decade
for year in data:
    # Replace the last digit of the year with zero
    decade = year['Year'][:-1] + "0"

    yearly_total = [0, 0] # [running total, number of entries]

    # average all months since some years may have "NaN" in the "J-D" column
    for month in months:
        if year[month] != "NaN":
            yearly_total[0] += float(year[month])
            yearly_total[1] += 1

    decade_means[decade][0] += yearly_total[0] / yearly_total[1]
    decade_means[decade][1] += 1

# Output the data to the console in a human readable format
for k, v in decade_means.items():
    mean = v[0] / v[1]
    print(f"{k}-{int(k)+v[1]-1}:  {mean:.4f}")



